import os
import tkinter as tk
from tkinter import filedialog
import pyautogui
import threading
import time

class AutoTypeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AUTO ESCRITOR")

        self.text_var = tk.StringVar()

        self.speed_var = tk.DoubleVar()
        self.speed_var.set(0.050)

        self.start_delay_var = tk.DoubleVar()
        self.start_delay_var.set(3)

        self.create_widgets()
        
        self.footer_label = tk.Label(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", bg="gray", fg="white", height=2)
        self.footer_label.pack(side=tk.BOTTOM, fill=tk.X)        
        self.root.state('zoomed')

    def create_widgets(self):
        tk.Label(self.root, text="DIGITE O TEXTO:").pack(pady=5)
        text_entry = tk.Text(self.root, wrap="word", width=50, height=10)
        text_entry.pack(pady=5)
        
        tk.Label(self.root, text="VELOCIDADE:").pack(pady=5)
        speed_scale = tk.Scale(self.root, from_=0.010, to=0.100, resolution=0.001, orient=tk.HORIZONTAL,
                               variable=self.speed_var, length=200)
        speed_scale.pack(pady=5)

        tk.Label(self.root, text="INICIAR EM:").pack(pady=5)
        start_delay_scale = tk.Scale(self.root, from_=1, to=10, resolution=1, orient=tk.HORIZONTAL,
                                     variable=self.start_delay_var, length=200)
        start_delay_scale.pack(pady=5)

        tk.Button(self.root, text="INICIAR", command=lambda: self.start_typing(text_entry)).pack(pady=10)
        tk.Button(self.root, text="LIMPAR", command=self.clear_fields).pack(pady=10)

    def start_typing(self, text_entry):
        text = text_entry.get("1.0", tk.END)
        speed = self.speed_var.get()
        start_delay = self.start_delay_var.get()

        self.root.iconify()  
        threading.Thread(target=self.type_text, args=(text, speed, start_delay)).start()

    def type_text(self, text, speed, start_delay):
        time.sleep(start_delay)
        pyautogui.write(text, interval=speed)

    def clear_fields(self):
        self.text_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoTypeApp(root)
    root.mainloop()
