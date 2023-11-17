from __future__ import annotations
from pathlib import Path
from typing import Optional, cast
from importlib.resources import as_file

from admon_parqueadero.baseDatos.deserializador import Deserializador
from admon_parqueadero.baseDatos.serializador import Serializador
from admon_parqueadero.gestorAplicacion.parqueadero.parqueadero import Parqueadero
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo
from admon_parqueadero.utils import ruta_archivos_programa


class BaseDatos:
    _RUTA_ARCHIVO = ruta_archivos_programa().joinpath("baseDatos/temp/datos.pkl")

    def __init__(self) -> None:
        self._parqueadero: Optional[Parqueadero] = None
        self._clientesResgistrados: dict[int, Cliente] = {}
        self._vehiculosRegistrados: dict[str, Vehiculo] = {}

    @classmethod
    def leerDatos(cls) -> Optional[BaseDatos]:
        # crear el directorio y el archivo en caso de que no exista
        with as_file(BaseDatos._RUTA_ARCHIVO) as archivo:
            deserializador = Deserializador(archivo)

        existenDatos = deserializador.existenDatos()

        basedatos: Optional[BaseDatos] = None
        if existenDatos:
            basedatos = cast(BaseDatos, deserializador.leerObjeto())
            return basedatos
        return basedatos

    def escribirDatos(self) -> None:
        serializador = Serializador()
        with as_file(BaseDatos._RUTA_ARCHIVO) as archivo:
            serializador.escribirObjeto(self, archivo)

    def buscarClienteRegistrado(self, cedula: int) -> Optional[Cliente]:
        return self._clientesResgistrados.get(cedula)

    def registrarCliente(self, cliente: Cliente) -> bool:
        if cliente.getCedula() in self._clientesResgistrados:
            return False
        self._clientesResgistrados[cliente.getCedula()] = cliente
        return True

    def buscarVehiculoRegistrado(self, placa: str) -> Optional[Vehiculo]:
        placa = placa.upper()
        return self._vehiculosRegistrados.get(placa)

    def registrarVehiculo(self, vehiculo: Vehiculo) -> bool:
        if vehiculo.getPlaca() in self._vehiculosRegistrados:
            return False
        self._vehiculosRegistrados[vehiculo.getPlaca()] = vehiculo
        return True

    def hayClientesRegistrados(self) -> bool:
        return not len(self._vehiculosRegistrados) == 0

    def hayVehiculosRegistrados(self) -> bool:
        return not len(self._vehiculosRegistrados) == 0

    def getParqueadero(self) -> Optional[Parqueadero]:
        return self._parqueadero

    def setParqueadero(self, parqueadero: Parqueadero) -> None:
        self._parqueadero = parqueadero
