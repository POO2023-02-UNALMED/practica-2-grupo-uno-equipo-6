from __future__ import annotations

from typing import Optional
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo


class Plaza:
    _plazasTotales: list[Plaza] = []

    def __init__(
        self,
        numeroPlaza: int,
        discapacitado: bool,
        tipo: str,
        vehiculo: Optional[Vehiculo],
    ) -> None:
        self._numeroPlaza = numeroPlaza
        self._discapacitado = discapacitado
        self._estado = "Disponible"
        self._vehiculo = vehiculo
        self._tipo = tipo
        Plaza._plazasTotales.append(self)

    def setDiscapacitado(self, discapacitado: bool) -> None:
        self._discapacitado = discapacitado

    def getDiscapacitado(self) -> bool:
        return self._discapacitado

    def setNumeroPlaza(self, numeroPlaza: int) -> None:
        self._numeroPlaza = numeroPlaza

    def getNumeroPlaza(self) -> int:
        return self._numeroPlaza

    def setEstado(self, estado: str) -> None:
        self._estado = estado

    def getEstado(self) -> str:
        return self._estado

    def setVehiculo(self, vehiculo: Optional[Vehiculo]) -> None:
        self._vehiculo = vehiculo

    def getVehiculo(self) -> Optional[Vehiculo]:
        return self._vehiculo

    def getTipo(self) -> str:
        return self._tipo

    def setTipo(self, tipo: str) -> None:
        self._tipo = tipo
