class equipos_electronico():

    def __init__(self) -> None:
        self.__tipo = ""
        self.__marca = ""
        self.__proveedor_usual = ""
        self.__años_garantia = ""

    def set_datos(self, tipo, marca, proveedor, años) -> None:
        self.__tipo = tipo
        self.__marca = marca
        self.__proveedor_usual = proveedor
        self.__años_garantia = años
    
    def get_datos(self) -> list:
        datos = []

        datos.append(self.__tipo)
        datos.append(self.__marca)
        datos.append(self.__proveedor_usual)
        datos.append(self.__años_garantia)
       
        return datos


        
        


        

    