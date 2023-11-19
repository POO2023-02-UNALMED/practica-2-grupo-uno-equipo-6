from __future__ import annotations
from typing import Optional

from admon_parqueadero.gestorAplicacion.parqueadero.tipo_estado import TipoEstado
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_producto import TipoProducto


class Producto:
    def __init__(self, tipo: TipoProducto, estado: TipoEstado, marca: Optional[str] = None) -> None:
        self._tipo = tipo
        self._marca = marca
        self._estado = estado
        self._precio = 0.0

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

    def getMarca(self) -> Optional[str]:
        return self._marca

    def setEstado(self, estado: TipoEstado) -> None:
        self._estado = estado

    def getEstado(self) -> TipoEstado:
        return self._estado

    def __eq__(self, otroProducto: object) -> bool:
        if not isinstance(otroProducto, Producto):
            return NotImplemented
        return id(self) == id(otroProducto)
