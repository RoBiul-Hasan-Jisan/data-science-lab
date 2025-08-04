import tkinter as tk
from tkinter import scrolledtext
import re

variables = {}
functions = {}

def evaluate_expression(expr):
    expr = expr.strip()
    for var in variables:
        expr = re.sub(rf'\b{var}\b', variables[var], expr)
    try:
        return str(eval(expr))
    except:
        return expr

def execute_block(block, output_widget):
    commands = [cmd.strip() for cmd in re.split(r';(?=(?:[^{}]*{[^}]*})*[^}]*$)', block) if cmd.strip()]

    for cmd in commands:
        if cmd.startswith("//") or not cmd:
            continue

        if cmd.startswith("liko "):
            msg = cmd[5:].strip()
            output_widget.insert(tk.END, evaluate_expression(msg) + "\n")

        elif cmd.startswith("let "):
            match = re.match(r"let\s+(\w+)\s*=\s*(.+)", cmd)
            if match:
                var, val = match.groups()
                variables[var] = evaluate_expression(val.strip())

        elif cmd.startswith("loop "):
            match = re.match(r"loop\s+(\d+)\s*{(.*)}", cmd, re.DOTALL)
            if match:
                count, loop_body = match.groups()
                for _ in range(int(count)):
                    execute_block(loop_body, output_widget)

        elif cmd.startswith("if "):
            match = re.match(r"if\s+(\w+)\s*==\s*(\w+)\s*{(.*)}\s*else\s*{(.*)}", cmd, re.DOTALL)
            if match:
                var1, var2, if_body, else_body = match.groups()
                if evaluate_expression(var1) == evaluate_expression(var2):
                    execute_block(if_body, output_widget)
                else:
                    execute_block(else_body, output_widget)

        elif cmd.startswith("func "):
            match = re.match(r"func\s+(\w+)\s*\(\)\s*{(.*)}", cmd, re.DOTALL)
            if match:
                fname, body = match.groups()
                functions[fname] = body

        elif re.match(r"\w+\(\);", cmd):
            fname = cmd.replace("();", "").strip()
            if fname in functions:
                execute_block(functions[fname], output_widget)
            else:
                output_widget.insert(tk.END, f"Function `{fname}` not found.\n")
        else:
            output_widget.insert(tk.END, f"Syntax Error: `{cmd}`\n")

def run_code(input_widget, output_widget):
    global variables, functions
    variables = {}
    functions = {}
    output_widget.delete(1.0, tk.END)
    code = input_widget.get(1.0, tk.END).strip()
    if code.startswith("{") and code.endswith("}"):
        body = code[1:-1].strip()
        execute_block(body, output_widget)
    else:
        output_widget.insert(tk.END, "Syntax Error: Code must be wrapped in { }\n")

def create_gui():
    window = tk.Tk()
    window.title("Toy Compiler")

    # Input area
    tk.Label(window, text="Write your code:").pack()
    input_box = scrolledtext.ScrolledText(window, height=15, width=70)
    input_box.pack()

    # Output area
    tk.Label(window, text="Output:").pack()
    output_box = scrolledtext.ScrolledText(window, height=10, width=70, bg="black", fg="white")
    output_box.pack()

    # Run button
    run_button = tk.Button(window, text="Run", command=lambda: run_code(input_box, output_box))
    run_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
