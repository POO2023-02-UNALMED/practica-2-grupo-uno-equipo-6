from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
    from admon_parqueadero.gestorAplicacion.parqueadero.plaza import Plaza


class Vehiculo:
    def __init__(
        self, placa: str, dueno: Optional[Cliente], marca: str, color: str, modelo: str
    ) -> None:
        self._placa = Vehiculo.normalizarPlaca(placa)
        self._dueno = dueno
        self._plaza: Optional[Plaza] = None
        self._marca = marca
        self._color = color
        self._modelo = modelo

    def getPlaca(self) -> str:
        return self._placa

    def setPlaca(self, placa: str) -> None:
        self._placa = Vehiculo.normalizarPlaca(placa)

    def getDueno(self) -> Optional[Cliente]:
        return self._dueno

    def setDueno(self, dueno: Cliente) -> None:
        self._dueno = dueno

    def getPlaza(self) -> Optional[Plaza]:
        return self._plaza

    def setPlaza(self, plaza: Optional[Plaza]) -> None:
        self._plaza = plaza

    def getMarca(self) -> str:
        return self._marca

    def setMarca(self, marca: str) -> None:
        self._marca = marca

    def getColor(self) -> str:
        return self._color

    def setColor(self, color: str) -> None:
        self._color = color

    def getModelo(self) -> str:
        return self._modelo

    def setModelo(self, modelo: str) -> None:
        self._modelo = modelo

    def estaParqueado(self) -> bool:
        """
        Este método retorna true si el vehículo se encuentra en el parqueadero, false si no lo está.
        El vehículo se considera parqueado si el atributo plaza no es null.
        """
        return self._plaza is not None

    def registradoPor(self, cliente: Cliente) -> bool:
        """
        Retorna true si el vehículo fue registrado por el cliente pasado como parámetro.
        """
        if self._dueno is not None:
            return self._dueno.getCedula() == cliente.getCedula()
        return False

    @staticmethod
    def normalizarPlaca(placa: str) -> str:
        """
        Devuelve la placa pasada como parámetro luego de hacerla mayúsculas y quitarle los espacios extra.
        """
        return placa.replace(" ", "").upper()
