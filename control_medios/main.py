import tkinter as tk
from tkinter import ttk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Main")

        label = ttk.Label(self, text="Selecciona la opción deseada")
        label.pack()

        btn1 = ttk.Button(self, text="Equipos electrónicos", command=self.open_equipos)
        btn1.pack(side='left')

        btn2 = ttk.Button(self, text="Inmuebles", command=self.open_inmuebles)
        btn2.pack(side='right')

    def open_equipos(self):
        self.destroy()
        from capa_presentacion import equipos
        equipos.Equipos()

    def open_inmuebles(self):
        self.destroy()
        from capa_presentacion import inmuebles
        inmuebles.Inmuebles()

if __name__ == "__main__":
    main = Main()
    main.mainloop()
