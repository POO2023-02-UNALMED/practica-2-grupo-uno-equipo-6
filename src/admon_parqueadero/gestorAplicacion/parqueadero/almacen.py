class Almacen:
    def __init__(self, capacidadMaxima: int) -> None:
        self._capacidadMaxima = capacidadMaxima

    def setCapacidadMaxima(self, capMax: int) -> None:
        self._capacidadMaxima = capMax

    def getCapacidadMaxima(self) -> int:
        return self._capacidadMaxima
