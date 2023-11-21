from enum import Enum


class MarcasCarro(Enum):
    TOYOTA = 60000000.0
    MAZDA = 70000000.0
    CHEVROLET = 90000000.0
    KIA = 80000000.0
    RENAULT = 55000000.0

    def getPrecioMaximo(self) -> float:
        return self.value
