import tkinter as tk
from tkinter import ttk

class Equipos(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Equipos")

        label = ttk.Label(self, text="Ventana de equipos electrónicos")
        label.pack()

        type_label = ttk.Label(self, text="Tipo:")
        type_label.pack()

        type_combo = ttk.Combobox(self, values=["Refrigerador", "TV", "Video", "Ventilador", "Aire Acondicionado", "Computadora"])
        type_combo.pack()

        brand_label = ttk.Label(self, text="Marca:")
        brand_label.pack()

        brand_combo = ttk.Combobox(self, values=["Sony", "Sanyo", "Panda", "LG"])
        brand_combo.pack()

        provider_label = ttk.Label(self, text="Proveedor:")
        provider_label.pack()

        provider_checkbox = ttk.Entry(self)
        provider_checkbox.pack()

        warranty_label = ttk.Label(self, text="Años de garantía:")
        warranty_label.pack()

        warranty_spinbox = tk.Spinbox(self, from_=1, to=5)
        warranty_spinbox.pack()
        
        back_btn = ttk.Button(self, text="Volver", command=self.back)
        back_btn.pack()

    def back(self):
        self.destroy()
        import main
        main.Main()
