from typing import Optional

from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.gestorAplicacion.parqueadero.plaza import Plaza


class Vehiculo:
    def __init__(
        self, placa: str, dueno: Cliente, marca: str, color: str, modelo: str
    ) -> None:
        self.placa = Vehiculo.normalizarPlaca(placa)
        self.dueno = dueno
        self.plaza: Optional[Plaza] = None
        self.marca = marca
        self.color = color
        self.modelo = modelo

    def getPlaca(self) -> str:
        return self.placa

    def setPlaca(self, placa: str) -> None:
        self.placa = Vehiculo.normalizarPlaca(placa)

    def getDueno(self) -> Cliente:
        return self.dueno

    def setDueno(self, dueno: Cliente) -> None:
        self.dueno = dueno

    def getPlaza(self) -> Optional[Plaza]:
        return self.plaza

    def setPlaza(self, plaza: Optional[Plaza]) -> None:
        self.plaza = plaza

    def getMarca(self) -> str:
        return self.marca

    def setMarca(self, marca: str) -> None:
        self.marca = marca

    def getColor(self) -> str:
        return self.color

    def setColor(self, color: str) -> None:
        self.color = color

    def getModelo(self) -> str:
        return self.modelo

    def setModelo(self, modelo: str) -> None:
        self.modelo = modelo

    def estaParqueado(self) -> bool:
        """
        Este método retorna true si el vehículo se encuentra en el parqueadero, false si no lo está.
        El vehículo se considera parqueado si el atributo plaza no es null.
        """
        return self.plaza is not None

    def registradoPor(self, cliente: Cliente) -> bool:
        """
        Retorna true si el vehículo fue registrado por el cliente pasado como parámetro.
        """
        return self.dueno.getCedula() == cliente.getCedula()

    @staticmethod
    def normalizarPlaca(placa: str) -> str:
        """
        Devuelve la placa pasada como parámetro luego de hacerla mayúsculas y quitarle los espacios extra.
        """
        return placa.replace(" ", "").upper()
