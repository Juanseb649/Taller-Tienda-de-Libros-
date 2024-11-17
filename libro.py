__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

import random
from Transaccion import Transaccion

class libro:
    #constructor
        def __init__(self, titulo: str, precioVenta: float, precioCompra: float, rutaImg: str):
    
    # Atributos
    
            self.__Cantidad = 0
            self.__titulo = titulo
            self.__rutaImg = rutaImg
            self.__precioVenta = precioVenta
            self.__precioCompra = precioCompra
            self.__Transacciones:list [list]
            self.__isbn = self.__crearIsbn(titulo)

        # Getters
        def getcantidad (self) -> str:
            return self.__Cantidad
        
        def getTitulo (self) -> str:
            return self.__titulo
        
        def getrutaImg (self) -> str:
            return self.__rutaImg
        
        def getprecioVenta (self) -> str:
            return self.__precioVenta
        
        def getprecioCompra (self)-> str:
            return self.__precioCompra
        
        def getTransacciones (self)-> list [Transaccion]:
            return self.__Transacciones
        
        def getisbn (self)-> str:
            return self.__isbn
        
            def getlibroMasCostoso (self) -> libro:
                return self.__libroMasCostoso
        
            def getLibroMasEconomico(self) -> Libro:
                return self.__LibroMasEconomico
        
        #Setters
        
        def setcantidad (self, cantidad, int):
            self.__Cantidad = cantidad
        
        def setTitulo (self, Titulo :str):
            self.__titulo = Titulo
        
        def setrutaImg (self, rutaImg: str):
            self.__rutaImg = rutaImg
        
        def setprecioVenta (self,precioVenta: float ):
            self.__precioVenta = precioVenta
        
        def setprecioCompra (self, precioCompra: float):
            self.__precioCompra = precioCompra
        
        def setisbn (self, isbn: str):
            self.__isbn = isbn
        
        #Vender
        
        def vender(self, cantidad: int, fecha: str) -> bool:
            if self.__cantidad >= cantidad:
                self.__transacciones.append(Transaccion)
            return True

        #Abastecer un libro
        
        def abastecer (self, cantidad: int, fecha: str) -> bool:
            Transaccion = Transaccion (Transaccion.ABASTECIMIENTO, cantidad, fecha)
            self.__cantidad += cantidad
            self.__Transacciones.append(Transaccion)
            return True