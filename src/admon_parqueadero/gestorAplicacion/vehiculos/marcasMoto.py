from enum import Enum


class MarcasMoto(Enum):
    YAMAHA = 5
    BAJAJ = 4
    HONDA = 3
    KTM = 2
    SUZUKI = 1

    def getOrdenPrecio(self) -> int:
        return self.value
