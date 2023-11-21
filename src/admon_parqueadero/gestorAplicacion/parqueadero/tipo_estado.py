#Funcionalidad del módulo: contiene un enum de con constantes del estado en 
#que se encuentra un vehiculo luego de haber sido revisado por un mecanico
#Componentes del módulo: TipoEstado
#Autores: Sofía, Sebastián, Alejandro, Sara, Katherine.



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
