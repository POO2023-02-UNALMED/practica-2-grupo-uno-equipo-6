from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.gestorAplicacion.personas.empleado import Empleado
from admon_parqueadero.gestorAplicacion.personas.persona import Persona

class Factura:
    def __init__(cliente: Cliente) -> None:
        self._cliente =  cliente