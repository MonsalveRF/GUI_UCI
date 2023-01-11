import tkinter as tk
from tkinter import ttk

class Inmuebles(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Inmuebes")

        label = ttk.Label(self, text="Ventana de inmuebles")
        label.pack()

        back_btn = ttk.Button(self, text="Volver", command=self.back)
        back_btn.pack()

    def back(self):
        self.destroy()
        import main
        main.Main()
