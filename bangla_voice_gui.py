import os
import json
import threading
import tkinter as tk
from tkinter import scrolledtext
from vosk import Model, KaldiRecognizer
import pyaudio
from PIL import Image, ImageTk
import time

# =============== CONFIGURATION ===============

MODEL_PATH = "vosk-model-small-en-us-0.15"
 # or "vosk-model-small-en-us-0.15"

# Mic icon image files
MIC_ON_IMG = "mic_on.png"
MIC_OFF_IMG = "mic_off.png"

# =============== CHECK MODEL ===============
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Model not found at: {MODEL_PATH}\nDownload it from: https://alphacephei.com/vosk/models")

# =============== LOAD VOSK MODEL ===============
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# =============== SETUP MICROPHONE ===============
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000,
                  input=True, frames_per_buffer=8192)
stream.start_stream()


# =============== MAIN APP CLASS ===============
class VoiceToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎤 Bangla Voice to Text")
        self.root.geometry("700x500")

        # --- Text Display ---
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Kalpurush", 14))
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # --- Load Mic Icons ---
        self.mic_on_img = ImageTk.PhotoImage(Image.open(MIC_ON_IMG).resize((40, 40)))
        self.mic_off_img = ImageTk.PhotoImage(Image.open(MIC_OFF_IMG).resize((40, 40)))
        self.icon_label = tk.Label(root, image=self.mic_off_img)
        self.icon_label.pack(pady=5)

        # --- Status & Timer ---
        self.status_label = tk.Label(root, text="🔴 Stopped", font=("Arial", 12))
        self.status_label.pack()

        self.timer_label = tk.Label(root, text="🕒 00:00", font=("Arial", 12))
        self.timer_label.pack()

        # --- Control Button ---
        self.recording = False
        self.button = tk.Button(root, text="🎙️ Start Listening", font=("Arial", 14),
                                command=self.toggle_recording)
        self.button.pack(pady=10)

        self.start_time = None

    def toggle_recording(self):
        if self.recording:
            self.recording = False
            self.button.config(text="🎙️ Start Listening")
            self.icon_label.config(image=self.mic_off_img)
            self.status_label.config(text="🔴 Stopped")
        else:
            self.recording = True
            self.start_time = time.time()
            self.button.config(text="⏹️ Stop Listening")
            self.icon_label.config(image=self.mic_on_img)
            self.status_label.config(text="🟢 Listening...")
            threading.Thread(target=self.listen_microphone, daemon=True).start()
            self.update_timer()

    def listen_microphone(self):
        while self.recording:
            data = stream.read(4096, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")
                print("[FULL]", text)  # 🔍 Debug print
                if text:
                    self.text_area.insert(tk.END, text + "\n")
                    self.text_area.see(tk.END)
            else:
                partial = json.loads(recognizer.PartialResult())
                print("[PARTIAL]", partial.get("partial", ""))  # 🔍 Debug partial

    def update_timer(self):
        if self.recording:
            elapsed = int(time.time() - self.start_time)
            minutes = elapsed // 60
            seconds = elapsed % 60
            self.timer_label.config(text=f"🕒 {minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="🕒 00:00")


# =============== RUN APP ===============
if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceToTextApp(root)
    root.mainloop()
