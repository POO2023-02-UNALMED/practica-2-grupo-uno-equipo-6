from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_producto import TipoProducto


class Almacen:
    _inventarioBase: dict[TipoProducto, float] = {}

    def __init__(self, capacidadMaxima: int) -> None:
        self._capacidadMaxima = capacidadMaxima
        self._inventario: list[Producto] = []

    def setCapacidadMaxima(self, capMax: int) -> None:
        self._capacidadMaxima = capMax

    def getCapacidadMaxima(self) -> int:
        return self._capacidadMaxima

    def setInventario(self, inventario: list[Producto]) -> None:
        self._inventario = inventario

    def getInventario(self) -> list[Producto]:
        return self._inventario

    @classmethod
    def setInventarioBase(cls, inventarioBase: dict[TipoProducto, float]) -> None:
        Almacen._inventarioBase = inventarioBase

    @classmethod
    def getInventarioBase(cls) -> dict[TipoProducto, float]:
        return Almacen._inventarioBase

    def agregarProducto(self, producto: Producto) -> None:
        self._inventario.append(producto)

    def conseguirProducto(self, tipoProducto: TipoProducto) -> Producto:
        for p in self._inventario:
            if p.getTipo() == tipoProducto:
                self._inventario.remove(p)
                return p
        return  # type: ignore

    @classmethod
    def cotizarProducto(cls, tipoProducto: TipoProducto) -> float:
        return Almacen._inventarioBase.get(tipoProducto)  # type: ignore

    def existeProducto(self, tipoProducto: TipoProducto) -> bool:
        for p in self._inventario:
            if p.getTipo() == tipoProducto:
                return True
        return False

    @classmethod
    def inicializarInventarioBase(cls) -> None:
        Almacen._inventarioBase[TipoProducto.TRANSMISION] = 4000000.0
        Almacen._inventarioBase[TipoProducto.AMORTIGUADOR] = 4000000.0
        Almacen._inventarioBase[TipoProducto.LLANTA] = 4000000.0
        Almacen._inventarioBase[TipoProducto.BATERIA] = 4000000.0
        Almacen._inventarioBase[TipoProducto.ACELERADOR] = 4000000.0
        Almacen._inventarioBase[TipoProducto.RIN] = 4000000.0
        Almacen._inventarioBase[TipoProducto.PEDAL] = 4000000.0
        Almacen._inventarioBase[TipoProducto.ACEITE] = 4000000.0
        Almacen._inventarioBase[TipoProducto.CADENA] = 4000000.0
        Almacen._inventarioBase[TipoProducto.GASOLINA] = 4000000.0
        Almacen._inventarioBase[TipoProducto.MOTOR] = 4000000.0
        Almacen._inventarioBase[TipoProducto.FRENO] = 4000000.0
        Almacen._inventarioBase[TipoProducto.PEDALES] = 4000000.0
        Almacen._inventarioBase[TipoProducto.LIQUIDOS] = 4000000.0
