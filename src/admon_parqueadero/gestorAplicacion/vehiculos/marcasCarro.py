from enum import Enum


class MarcasCarro(Enum):
    TOYOTA = 51000000.0
    MAZDA = 52000000.0
    CHEVROLET = 53000000.0
    KIA = 54000000.0
    RENAULT = 55000000.0

    def getPrecioMaximo(self) -> float:
        return self.value
