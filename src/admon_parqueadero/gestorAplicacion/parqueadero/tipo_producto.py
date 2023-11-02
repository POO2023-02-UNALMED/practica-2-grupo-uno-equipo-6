from enum import Enum, auto


class TipoProducto(Enum):
    MOTOR = auto()
    TRANSMISION = auto()
    ACELERADOR = auto()
    FRENO = auto()
    BATERIA = auto()
    GASOLINA = auto()
    ACEITE = auto()
    LIQUIDOS = auto()
    LLANTA = auto()
    RIN = auto()
    PEDAL = auto()
    CADENA = auto()
    PEDALES = auto()
    AMORTIGUADOR = auto()

    def __str__(self) -> str:
        return self.name.title()
