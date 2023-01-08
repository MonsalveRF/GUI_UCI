import tkinter as tk
from equipos_electronicos import *

# Crea la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de interfaz con tkinter")

# Crea los labels
tk.Label(ventana, text="Tipo:").grid(row=0, column=0)
tk.Label(ventana, text="Marca:").grid(row=1, column=0)
tk.Label(ventana, text="Proveedor:").grid(row=2, column=0)
tk.Label(ventana, text="Años de garantía:").grid(row=3, column=0)

# Crea el primer listbox
tipos = ["Refrigerador", "TV", "Video", "Ventilador", "Aire Acondicionado", "Computadora"]
tipo_seleccionado = tk.StringVar(ventana)
tipo_seleccionado.set(tipos[0])
opciones_tipo = tk.OptionMenu(ventana, tipo_seleccionado, *tipos)
opciones_tipo.grid(row=0, column=1)

# Crea el segundo listbox
marcas = ["Sony", "Sanyo", "Panda", "LG"]
marca_seleccionada = tk.StringVar(ventana)
marca_seleccionada.set(marcas[0])
opciones_marca = tk.OptionMenu(ventana, marca_seleccionada, *marcas)
opciones_marca.grid(row=1, column=1)

# Crea los textboxes
proveedor = tk.Entry(ventana)
proveedor.grid(row=2, column=1)
garantia = tk.Entry(ventana)
garantia.grid(row=3, column=1)

# Crea el botón
def almacenar_valores():
  tipo = tipo_seleccionado.get()
  marca = marca_seleccionada.get()
  proveedor_valor = proveedor.get()
  garantia_valor = garantia.get()
  
  nuevo = equipos_electronico()
  nuevo.set_datos(tipo,marca,proveedor_valor,garantia_valor)
  print(nuevo.get_datos())

  
boton = tk.Button(ventana, text="Almacenar", command=almacenar_valores)
boton.grid(row=4, column=0, columnspan=2)

# Muestra la ventana
ventana.mainloop()
