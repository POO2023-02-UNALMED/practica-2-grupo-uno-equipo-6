from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_estado import TipoEstado
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_producto import TipoProducto
from admon_parqueadero.gestorAplicacion.vehiculos.marcasCarro import MarcasCarro


class Producto:
    def __init__(self, tipo: TipoProducto, marca: str, estado: TipoEstado) -> None:
        self._tipo = tipo
        self._marca = ""
        self._estado = estado
        self._precio = 0

    def setTipo(self, tipo: TipoProducto) -> None:
        self._tipo = tipo

    def getTipo(self) -> TipoProducto:
        return self._tipo

    def setPrecio(self, precio: float) -> None:
        self._precio = precio

    def getPrecio(self) -> float:
        return self._precio

    def setMarca(self, marca: str) -> None:
        self._marca = marca

    def getMarca(self) -> str:
        return self._marca

    def setEstado(self, estado: TipoEstado) -> None:
        self._estado = estado

    def getEstado(self) -> TipoEstado:
        return self._estado

    def __eq__(self, otroProducto: Producto) -> bool:
        return id(self) == id(otroProducto)
