from typing import Optional
from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_producto import TipoProducto


class Almacen:

    def __init__(self, capacidadMaxima: int) -> None:
        self._capacidadMaxima = capacidadMaxima
        self._inventario: list[Producto] = []
        self._inventarioBase: dict[TipoProducto, float] = {}
        self.inicializarInventarioBase()


    def setCapacidadMaxima(self, capMax: int) -> None:
        self._capacidadMaxima = capMax

    def getCapacidadMaxima(self) -> int:
        return self._capacidadMaxima

    def setInventario(self, inventario: list[Producto]) -> None:
        self._inventario = inventario

    def getInventario(self) -> list[Producto]:
        return self._inventario

    def setInventarioBase(self, inventarioBase: dict[TipoProducto, float]) -> None:
        self._inventarioBase = inventarioBase

    
    def getInventarioBase(self) -> dict[TipoProducto, float]:
        return self._inventarioBase

    def agregarProducto(self, producto: Producto) -> None:
        self._inventario.append(producto)

    def conseguirProducto(self, tipoProducto: TipoProducto) -> Optional[Producto]:
        for p in self._inventario:
            if p.getTipo() == tipoProducto:
                self._inventario.remove(p)
                return p
        return None

    def cotizarProducto(self, tipoProducto: TipoProducto) -> float:
        return self._inventarioBase.get(tipoProducto, 0)

    def existeProducto(self, tipoProducto: TipoProducto) -> bool:
        for p in self._inventario:
            if p.getTipo() == tipoProducto:
                return True
        return False

    def inicializarInventarioBase(self) -> None:
        self._inventarioBase[TipoProducto.TRANSMISION] = 4000000.0
        self._inventarioBase[TipoProducto.AMORTIGUADOR] = 4000000.0
        self._inventarioBase[TipoProducto.LLANTA] = 4000000.0
        self._inventarioBase[TipoProducto.BATERIA] = 4000000.0
        self._inventarioBase[TipoProducto.ACELERADOR] = 4000000.0
        self._inventarioBase[TipoProducto.RIN] = 4000000.0
        self._inventarioBase[TipoProducto.PEDAL] = 4000000.0
        self._inventarioBase[TipoProducto.ACEITE] = 4000000.0
        self._inventarioBase[TipoProducto.CADENA] = 4000000.0
        self._inventarioBase[TipoProducto.GASOLINA] = 4000000.0
        self._inventarioBase[TipoProducto.MOTOR] = 4000000.0
        self._inventarioBase[TipoProducto.FRENO] = 4000000.0
        self._inventarioBase[TipoProducto.PEDALES] = 4000000.0
        self._inventarioBase[TipoProducto.LIQUIDOS] = 4000000.0
