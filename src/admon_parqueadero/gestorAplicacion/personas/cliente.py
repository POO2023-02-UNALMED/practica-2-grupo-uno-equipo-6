from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from admon_parqueadero.gestorAplicacion.parqueadero.factura import Factura
from admon_parqueadero.gestorAplicacion.personas.persona import Persona

if TYPE_CHECKING:
    from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo


class Cliente(Persona):
    def __init__(
        self,
        nombre: str,
        cedula: int,
        telefono: int,
        correo: str,
        direccion: str,
        discapacitado: bool,
    ) -> None:
        super().__init__(nombre, cedula, telefono, correo, direccion)
        self._discapacitado = discapacitado
        self._factura = Factura(self)
        self._vehiculos: list[Vehiculo] = []

    def agregarVehiculo(self, vehiculo: Vehiculo) -> None:
        self._vehiculos.append(vehiculo)

    def setDiscapacitado(self, disc: bool) -> None:
        self._discapacitado = disc

    def isDiscapacitado(self) -> bool:
        return self._discapacitado

    def setFactura(self, factura: Optional[Factura]) -> None:
        self._factura = factura

    def getFactura(self) -> Optional[Factura]:
        return self._factura

    def setVehiculos(self, vehiculos: list[Vehiculo]) -> None:
        self._vehiculos = vehiculos

    def getVehiculos(self) -> list[Vehiculo]:
        return self._vehiculos
