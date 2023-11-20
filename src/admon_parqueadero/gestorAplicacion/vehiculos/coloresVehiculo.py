from enum import Enum, auto


class ColoresVehiculo(Enum):
    ROJO = auto()
    AZUL = auto()
    VERDE = auto()
    MORADO = auto()
    NARANJA = auto()
    GRIS = auto()
    NEGRO = auto()
    BLANCO = auto()
    ROSADO = auto()
    AMARILLO = auto()

    @classmethod
    def lista(cls):
        return [x.name.title() for x in cls]
