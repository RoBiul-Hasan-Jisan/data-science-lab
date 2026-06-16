import re

variables = {}
functions = {}

def evaluate_expression(expr):
    expr = expr.strip()
    if expr in variables:
        return variables[expr]
    return expr

def execute_block(block):
    commands = [cmd.strip() for cmd in re.split(r';(?=(?:[^{}]*{[^}]*})*[^}]*$)', block) if cmd.strip()]

    for cmd in commands:
        if cmd.startswith("//") or not cmd:
            continue

        if cmd.startswith("liko "):
            msg = cmd[5:].strip()
            print(evaluate_expression(msg))

        elif cmd.startswith("let "):
            match = re.match(r"let\s+(\w+)\s*=\s*(.+)", cmd)
            if match:
                var, val = match.groups()
                variables[var] = val.strip()

        elif cmd.startswith("loop "):
            match = re.match(r"loop\s+(\d+)\s*{(.*)}", cmd, re.DOTALL)
            if match:
                count, loop_body = match.groups()
                for _ in range(int(count)):
                    execute_block(loop_body)

        elif cmd.startswith("if "):
            match = re.match(r"if\s+(\w+)\s*==\s*(\w+)\s*{(.*)}\s*else\s*{(.*)}", cmd, re.DOTALL)
            if match:
                var1, var2, if_body, else_body = match.groups()
                if evaluate_expression(var1) == evaluate_expression(var2):
                    execute_block(if_body)
                else:
                    execute_block(else_body)

        elif cmd.startswith("func "):
            match = re.match(r"func\s+(\w+)\s*\(\)\s*{(.*)}", cmd, re.DOTALL)
            if match:
                fname, body = match.groups()
                functions[fname] = body

        elif re.match(r"\w+\(\);", cmd):
            fname = cmd.replace("();", "").strip()
            if fname in functions:
                execute_block(functions[fname])
            else:
                print(f"Function `{fname}` not found.")

        else:
            print(f"Syntax Error: Unknown command `{cmd}`")

# ---- Run the compiler with sample input ----
if __name__ == "__main__":
    code = """
    {
        let name = Jisan;
        liko Hello;
        liko name;
        
        loop 2 {
            liko Looping...;
        }

        if name == Jisan {
            liko You're Jisan!;
        } else {
            liko You're not Jisan;
        }

        func greet() {
            liko Hello from function!;
        }

        greet();
    }
    """
    code = code.strip()
    if code.startswith("{") and code.endswith("}"):
        body = code[1:-1].strip()
        execute_block(body)
    else:
        print("Syntax Error: Code must be wrapped in { }")
