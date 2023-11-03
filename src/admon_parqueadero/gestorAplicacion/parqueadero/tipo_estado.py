from __future__ import annotations

from enum import Enum


class TipoEstado(Enum):
    MAL_ESTADO = 0
    BUEN_ESTADO = 1
    EXCELENTE_ESTADO = 2

    def getEstado(self) -> int:
        return self.value

    @classmethod
    def segunNumero(cls, estado: int) -> TipoEstado:
        return cls(estado)
