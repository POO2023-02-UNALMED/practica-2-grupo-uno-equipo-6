class Almacen:
    def __init__(capacidadMaxima: int) -> None:
        self._capacidadMaxima = capacidadMaxima

    def setCapacidadMaxima(self, capMax) -> None:
        self._capacidadMaxima = capMax

    def getCapacidadMaxima(self) -> int:
        return self._capacidadMaxima

    