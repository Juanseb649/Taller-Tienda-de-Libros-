__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

from enum import Enum

class TipoTransaccion(Enum):
    ABASTECIMIENTO = 1
    VENTA = 2

class Transaccion:
    
    # Constructor
    
    def __init__(self, tipo: TipoTransaccion, cantidad: int, fecha: str):
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = fecha
        
    
    # Atributos
    
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__fecha = fecha
    
    # Metodos
    
    #Getters
    def getTipo(self) -> TipoTransaccion:
        return self.__tipo
    
    def getCantidad(self) -> int:
        return self.__cantidad
    
    def getFecha(self) -> str:
        return self.__fecha
    
    #Setters
    def setTipo(self, tipo: TipoTransaccion):
        self.__tipo = tipo
    
    def setCantidad(self, cantidad: int):
        self.__cantidad = cantidad
    
    def setFecha(self, fecha: str):
        self.__fecha = fecha