from typing import Optional, Union
from admon_parqueadero.gestorAplicacion.parqueadero.almacen import Almacen
from admon_parqueadero.gestorAplicacion.parqueadero.plaza import Plaza
from admon_parqueadero.gestorAplicacion.personas.empleado import Empleado
from admon_parqueadero.gestorAplicacion.vehiculos.carro import Carro
from admon_parqueadero.gestorAplicacion.vehiculos.moto import Moto
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo


class Parqueadero:
    def __init__(
        self,
        plazasTotales: int,
        tarifaCarro: float,
        tarifaMoto: float,
        almacen: Almacen,
    ) -> None:
        self._plazasTotales = plazasTotales
        self._plazasDisponibles = plazasTotales
        self._tarifacarro = tarifaCarro
        self._tarifaMoto = tarifaMoto
        self._plazas: list[Plaza] = []
        self._empleados: list[Empleado] = []
        self._almacen = almacen
        self._administrador: Optional[Empleado] = None
        self._vehiculosVenta: list[Carro] = []

    def getVehiculosVenta(self) -> list[Carro]:
        return self._vehiculosVenta

    def setVehiculosVenta(self, vehiculosVenta: list[Carro]) -> None:
        self._vehiculosVenta = vehiculosVenta

    def getPlazasTotales(self) -> int:
        return self._plazasTotales

    def setPlazasTotales(self, plazasTotales: int) -> None:
        self._plazasTotales = plazasTotales

    def getPlazasDisponibles(self) -> int:
        return self._plazasDisponibles

    def setPlazasDisponibles(self, plazasDisponibles: int) -> None:
        self._plazasDisponibles = plazasDisponibles

    def getTarifaCarro(self) -> float:
        return self._tarifacarro

    def setTarifaCarro(self, tarifaCarro: float) -> None:
        self._tarifacarro = tarifaCarro

    def getTarifaMoto(self) -> float:
        return self._tarifaMoto

    def setTarifaMoto(self, tarifaMoto: float) -> None:
        self._tarifaMoto = tarifaMoto

    def getPlazas(self) -> list[Plaza]:
        return self._plazas

    def setPlazas(self, plazas: list[Plaza]) -> None:
        self._plazas = plazas

    def getEmpleados(self) -> list[Empleado]:
        return self._empleados

    def setEmpleados(self, empleados: list[Empleado]) -> None:
        self._empleados = empleados

    def getAlmacen(self) -> Almacen:
        return self._almacen

    def setAlmacen(self, almcaen: Almacen) -> None:
        self._almacen = almcaen

    def getAdministrador(self) -> Optional[Empleado]:
        return self._administrador

    def setAdministrador(self, administrador: Empleado) -> None:
        self._administrador = administrador

    def getMecanicos(self) -> list[Empleado]:
        return [
            empleado
            for empleado in self._empleados
            if empleado.getCargo() == "Mecanico"
        ]

    def setVendedores(self) -> list[Empleado]:
        return [
            vendedor
            for vendedor in self._empleados
            if vendedor.getCargo() == "Vendedor"
        ]

    def agregarVehiculoVenta(self, vehiculo: Carro) -> None:
        self._vehiculosVenta.append(vehiculo)

    def agregarEmpleado(self, empleado: Empleado) -> None:
        self._empleados.append(empleado)

    def existeEmpleado(self, cedula: int) -> bool:
        for e in self._empleados:
            if e.getCedula() == cedula:
                return True
        return False

    def agregarPlazas(self, cantidad: int, discapacitado: bool, tipo: str) -> None:
        self._plazasTotales += cantidad
        ultimoNumPlaza = self._plazas[-1].getNumeroPlaza()
        for _ in range(cantidad):
            self._plazas.append(Plaza(ultimoNumPlaza + 1, discapacitado, None, tipo))  # type: ignore
            ultimoNumPlaza += 1

    def ingresarVehiculo(self, vehiculo: Vehiculo, plaza: Plaza) -> None:
        # si esta plaza ya tiene un vehiculo, entonces desasociarlo
        if plaza.getVehiculo() != None:
            plaza.getVehiculo().setPlaza(None)

        plaza.setVehiculo(vehiculo)

        # asignar el estado de la plaza y la plaza al vehiculo
        if vehiculo == None:
            plaza.setEstado("Disponible")
        else:
            plaza.setEstado("No disponible")
            vehiculo.setPlaza(plaza)

    def retirarVehiculo(self, key: Union[int, str]) -> None:
        if isinstance(key, int):
            plaza = self._plazas[key - 1]
            plaza.getVehiculo().setPlaza(None)
            plaza.setVehiculo(None)  # type: ignore
            plaza.setEstado("Disponible")
        else:
            for p in self._plazas:
                if p.getVehiculo() != None and p.getVehiculo().getPlaca() == key:
                    p.getVehiculo().setPlaza(None)
                    p.setVehiculo(None)  # type: ignore
                    p.setEstado("Disponible")

    def plazasDisponiblesPara(self, vehiculo: Vehiculo) -> list[Plaza]:
        plazasDisponibles: list[Plaza] = []
        tipo = ""
        if isinstance(vehiculo, Carro):
            tipo = "Carro"
        else:
            moto: Moto = vehiculo  # type: ignore
            if moto.getTipo() == "normal":
                tipo = "Moto"
            else:
                tipo = "Moto altoCC"

        for p in self._plazas:
            if p.getTipo() == tipo and p.getEstado() == "Disponible":
                plazasDisponibles.append(p)
        return plazasDisponibles

    def buscarPlaza(self, numeroPlaza: int) -> Optional[Plaza]:
        for p in self._plazas:
            if p.getNumeroPlaza() == numeroPlaza:
                return p
        return None
