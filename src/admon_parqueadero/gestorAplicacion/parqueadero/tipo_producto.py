#Funcionalidad del módulo: contiene un enum 
#de constantes equivalente a los productos de un vehiculo
#tanto de carro como para moto
#Componentes del módulo: TipoProducto
#Autores: Sebastián, Alejandro, Sara, Sofía, Katherine.




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
