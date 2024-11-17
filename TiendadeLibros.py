__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"


from libro import libro
class TiendaDeLibros:
    
    #constructor
    def __init__(self):
    
    #Atributos
        self.__caja = 0.0
        self.__CatalogoDeLibros : list[libro] = []
    
    # Getters
    def getcaja (self) -> float:
        return self.__caja
    
    def getcajaCatalogoDeLibors (self) -> list[libro]:
        return self.__CatalogoDeLibros
    
    # Setters
    def setcaja (self, caja: float):
        self.__caja = caja
    
    
    # Registrar un libro en catalogo
    
    def registrarLibro (self, nombre: str, precioVenta: float, precioCompra: float, rutaimg:str):
        libro = libro(nombre, precioVenta,precioCompra, rutaimg)
    
    # Busqueda de libro (titulo,isbn)
    
    def buscarLibroporTitulo(self, titulo: str) -> libro:
        for libro in self.__CatalogoDeLibros:
            if libro.getTitulo() == titulo:
                return libro
    
    def buscarLibroporisbn(self, isbn: str)-> libro:
        for libro in self.__CatalogoDeLibros:
            if libro.getisbn ()== isbn:
                return libro
            return None
        
    # Devolver el libro mas costoso
    
            def getLibroMasCostoso(self) -> libro:
                if len(self.__CatalogoDeLibros) == 0:
                    return None
        libroMasCostoso = self.__CatalogoDeLibros[0]
        for libro in self.__CatalogoDeLibros:
            if libro.getPrecioVenta() > libroMasCostoso.getprecioVenta():
                libroMasCostoso = libro
            return libroMasCostoso
    
    # Devolver el libro mas ecomomico
    
            def getLibroMasEconomico (self)-> libro:
                if len(self.__CatalogoDeLibros) == 0:
                    return None
        libroMasEconomico = self.__CatalogoDeLibros[0]
        for libro in self.__CatalogoDeLibros:
            if libro.getPrecioCompra() < libroMasEconomico.getPrecioCompra():
                libroMasEconomico = libro
        return libroMasEconomico
    
    #Devuelve la cantidad de transacciones de tipo ABASTECIMIENTO
    
    def getCantidadTransaccionesAbastecimiento(self, isbn: str) -> int:
        libro = self.buscarLibroPorIsbn(isbn)
        if libro != None:
            return len(libro.getTransacciones())
        return 0
    