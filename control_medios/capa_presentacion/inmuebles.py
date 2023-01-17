import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from capa_negocios.mobiliario import *

class Inmuebles(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Inmuebes")

        label = ttk.Label(self, text="Ventana de inmuebles")
        label.pack()

        # Agregando los labels
        tipo_label = ttk.Label(self, text="Tipo")
        tipo_label.pack()

        # Agregando el combobox del tipo
        self.tipo_combobox = ttk.Combobox(self, values=["Silla", "Mesa", "Cama", "Mueble", "PC"])
        self.tipo_combobox.pack()

        proveedor_label = ttk.Label(self, text="Proveedor")
        proveedor_label.pack()

        # Agregando el entry del proveedor
        self.proveedor_entry = ttk.Entry(self)
        self.proveedor_entry.pack()

        tiempo_label = ttk.Label(self, text="Tiempo Estimado")
        tiempo_label.pack()

        # Agregando el spinbox del tiempo estimado
        self.tiempo_spinbox = ttk.Spinbox(self, from_=1, to=8)
        self.tiempo_spinbox.pack()

        local_label = ttk.Label(self, text="Local")
        local_label.pack()        

        # Agregando el combobox del local        
        self.local_combobox = ttk.Combobox(self, values=["Laboratorio", "Aula", "Departamento", "Oficina"])
        self.local_combobox.pack()

        # Agregando el boton "registrar"
        registrar_btn = ttk.Button(self, text="Registrar", command=self.register)
        registrar_btn.pack(side='left')

        # Agregando el boton "Volver"
        back_btn = ttk.Button(self, text="Volver", command=self.back)
        back_btn.pack(side='right')

    def register(self):
        if self.tipo_combobox.get()=="" or self.proveedor_entry.get()=="" or self.tiempo_spinbox.get()=="" or self.local_combobox.get()=="":
            tk.messagebox.showwarning("Error","Por favor selecciona toda la informacion requerida")
        else:
            nuevo = Mobiliario_UCI()
            nuevo.set_datos(self.tipo_combobox.get(),self.proveedor_entry.get(),self.tiempo_spinbox.get(),self.local_combobox.get())
            tk.messagebox.showinfo("Registro Exitoso","Datos Ingresados Correctamente")
            self.tipo_combobox.delete(0,tk.END)
            self.tiempo_spinbox.delete(0,tk.END)
            self.proveedor_entry.delete(0,tk.END)
            self.local_combobox.delete(0,tk.END)

           
            print(nuevo.get_datos())


    def back(self):
        self.destroy()
        import main
        main.Main()
