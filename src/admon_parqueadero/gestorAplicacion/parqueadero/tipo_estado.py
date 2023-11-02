from enum import Enum
from typing import Self


class TipoEstado(Enum):
    MAL_ESTADO = 0
    BUEN_ESTADO = 1
    EXCELENTE_ESTADO = 2

    def getEstado(self) -> int:
        return self.value

    @classmethod
    def segunNumero(cls, estado: int) -> Self:
        return cls(estado)
