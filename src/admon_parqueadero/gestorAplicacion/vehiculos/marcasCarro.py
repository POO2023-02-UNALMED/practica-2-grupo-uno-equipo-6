from enum import Enum


class MarcasCarro(Enum):
    TOYOTA = 50000000.0
    MAZDA = 50000000.0
    CHEVROLET = 50000000.0
    KIA = 50000000.0
    RENAULT = 50000000.0

    def getPrecioMaximo(self) -> float:
        return self.value
