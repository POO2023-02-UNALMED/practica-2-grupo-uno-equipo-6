class Producto:
    
    def __eq__(self, otroProducto: Producto) -> bool:
        return id(self) == id(otroProducto)
