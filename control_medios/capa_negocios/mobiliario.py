class Mobiliario_UCI():
    def __init__(self) -> None:
        self.__tipo = ""
        self.__proveedor = ""
        self.__tiempo_estimado = ""
        self.__local = ""

    def set_datos(self, tipo, proveedor, tiempo, local) -> None:
        self.__tipo = tipo
        self.__proveedor = proveedor
        self.__tiempo_estimado = tiempo
        self.__local = local

    def get_datos(self) -> list:
        datos = []

        datos.append(self.__tipo)
        datos.append(self.__proveedor)
        datos.append(self.__tiempo_estimado)
        datos.append(self.__local)

        return datos