import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Equipos(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Equipos")
        self.all_data=[]

        label = ttk.Label(self, text="Ventana de equipos electrónicos")
        label.pack()

        self.type_label = ttk.Label(self, text="Tipo:")
        self.type_label.pack()

        self.type_combo = ttk.Combobox(self, values=["Refrigerador", "TV", "Video", "Ventilador", "Aire Acondicionado", "Computadora"])
        self.type_combo.pack()

        brand_label = ttk.Label(self, text="Marca:")
        brand_label.pack()

        self.brand_combo = ttk.Combobox(self, values=["Sony", "Sanyo", "Panda", "LG"])
        self.brand_combo.pack()

        provider_label = ttk.Label(self, text="Proveedor:")
        provider_label.pack()

        self.provider_entry = ttk.Entry(self)
        self.provider_entry.pack()

        warranty_label = ttk.Label(self, text="Años de garantía:")
        warranty_label.pack()

        self.warranty_spinbox = tk.Spinbox(self, from_=1, to=5)
        self.warranty_spinbox.pack()
        
        back_btn = ttk.Button(self, text="Volver", command=self.back)
        back_btn.pack(side='left')

        register_btn = ttk.Button(self, text="Registrar", command=self.register)
        register_btn.pack(side='right')

    def back(self):
        self.destroy()
        import main
        main.Main()
        
    def register(self):
        if self.provider_entry.get()=="" or self.type_combo.get()=="" or self.brand_combo.get()=="" or self.warranty_spinbox.get()=="":
            tk.messagebox.showwarning("Error","Por favor selecciona toda la informacion requerida")
        else:
            self.all_data.append({"tipo":self.type_combo.get(),"marca":self.brand_combo.get(),"proveedor":self.provider_entry.get(),"garantía":self.warranty_spinbox.get()})
            tk.messagebox.showinfo("Registro Exitoso","Datos Ingresados Correctamente")
            self.provider_entry.delete(0,tk.END)
            self.type_combo.delete(0,tk.END)
            self.brand_combo.delete(0,tk.END)
            self.warranty_spinbox.delete(0,tk.END)
