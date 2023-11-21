#Funcionalidad del módulo: contiene la clase Carro que representa un carro de la vida real
#Componentes del módulo: Carro
#Autores: Alejandro, Sebastián

from typing import Optional

import random
from admon_parqueadero.errores import ErrorLogicaIncorrecta
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.gestorAplicacion.vehiculos.tipo_vehiculo import TipoVehiculo
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_producto import TipoProducto
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_estado import TipoEstado
from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto


class Carro(Vehiculo):
    def __init__(
        self,
        placa: str,
        dueno: Optional[Cliente],
        marca: str,
        color: str,
        modelo: str,
        tipo: TipoVehiculo,
        puestos: int,
        discapacitado: bool,
        precioVenta: Optional[float] = None,
    ):
        super().__init__(placa, dueno, marca, color, modelo)
        self._tipo = tipo
        self._puestos = puestos
        self._motor = self._inicializarProducto(TipoProducto.MOTOR)
        self._transmision = self._inicializarProducto(TipoProducto.TRANSMISION)
        self._acelerador = self._inicializarProducto(TipoProducto.ACELERADOR)
        self._freno = self._inicializarProducto(TipoProducto.FRENO)
        self._bateria = self._inicializarProducto(TipoProducto.BATERIA)
        self._pedal = self._inicializarProducto(TipoProducto.PEDAL)
        self._precioVenta = 0.0
        self._discapacitado = discapacitado
        self._inicializarDepositos()
        self._inicializarLlantas()
        self._inicializarRines()
        self._inicializarAmortiguadores()

        if precioVenta is not None:
            self._precioVenta = precioVenta
            self._motor.setEstado(TipoEstado.EXCELENTE_ESTADO)
            self._acelerador.setEstado(TipoEstado.EXCELENTE_ESTADO)
            self._freno.setEstado(TipoEstado.EXCELENTE_ESTADO)
            self._bateria.setEstado(TipoEstado.EXCELENTE_ESTADO)
            self._pedal.setEstado(TipoEstado.EXCELENTE_ESTADO)
            self._transmision.setEstado(TipoEstado.EXCELENTE_ESTADO)
            for p in self._depositos:
                p.setEstado(TipoEstado.EXCELENTE_ESTADO)
            for p in self._llantas:
                p.setEstado(TipoEstado.EXCELENTE_ESTADO)
            for p in self._rines:
                p.setEstado(TipoEstado.EXCELENTE_ESTADO)
            for p in self._amortiguadores:
                p.setEstado(TipoEstado.EXCELENTE_ESTADO)

    def isDiscapacitado(self) -> bool:
        return self._discapacitado

    def setDiscapacitado(self, discapacitado: bool) -> None:
        self._discapacitado = discapacitado

    def getPrecioVenta(self) -> float:
        return self._precioVenta

    def setPrecioVenta(self, precioVenta: float) -> None:
        if precioVenta < 0:
            raise ErrorLogicaIncorrecta("precioVenta no puede ser menor a 0")
        self._precioVenta = precioVenta

    def getTipo(self) -> str:
        return self._tipo.name

    def setTipo(self, tipo: TipoVehiculo) -> None:
        if tipo == TipoVehiculo.ALTOCC or tipo == TipoVehiculo.NORMAL:
            raise ErrorLogicaIncorrecta("tipo de carro no puede ser ALTOCC ni NORMAL")
        self._tipo = tipo

    def getPuestos(self) -> int:
        return self._puestos

    def setPuestos(self, puestos: int) -> None:
        if puestos < 0:
            raise ErrorLogicaIncorrecta("puestos no puede ser negativo")
        self._puestos = puestos

    def getMotor(self) -> Producto:
        return self._motor

    def setMotor(self, motor: Producto) -> None:
        self._motor = motor

    def getTransmision(self) -> Producto:
        return self._transmision

    def setTransmision(self, transmision: Producto) -> None:
        self._transmision = transmision

    def getAcelerador(self) -> Producto:
        return self._acelerador

    def setAcelerador(self, acelerador: Producto) -> None:
        self._acelerador = acelerador

    def getFreno(self) -> Producto:
        return self._freno

    def setFreno(self, freno: Producto) -> None:
        self._freno = freno

    def getBateria(self) -> Producto:
        return self._bateria

    def setBateria(self, bateria: Producto) -> None:
        self._bateria = bateria

    def getPedal(self) -> Producto:
        return self._pedal

    def setPedal(self, pedal: Producto) -> None:
        self._pedal = pedal

    def getDepositos(self) -> list[Producto]:
        return self._depositos

    def setDepositos(self, depositos: list[Producto]) -> None:
        self._depositos = depositos

    def getLlantas(self) -> list[Producto]:
        return self._llantas

    def setLlantas(self, llantas: list[Producto]) -> None:
        self._llantas = llantas

    def getRines(self) -> list[Producto]:
        return self._rines

    def setRines(self, rines: list[Producto]) -> None:
        self._rines = rines

    def getAmortiguadores(self) -> list[Producto]:
        return self._amortiguadores

    def setAmortiguadores(self, amortiguadores: list[Producto]) -> None:
        self._amortiguadores = amortiguadores

    def __str__(self) -> str:
        placa = self.getPlaca()
        marca = self.getMarca().title()
        modelo = self.getModelo().title()
        color = self.getColor().title()
        tipo = self.getTipo().title()
        puestos = self.getPuestos()
        if self._precioVenta != 0:  # para los carros para venta se imprime su valor
            precioVenta = round(self.getPrecioVenta(), 2)
            return f"{placa} {marca} {modelo} {color}\n{tipo} {puestos} puestos\nPrecio: {precioVenta}"
        return f"{placa} {marca} {modelo} {color}\n{tipo} {puestos} puestos\n"

    # metodo que crea cuatro Productos tipo llanta y los agrega al array self._llantas
    def _inicializarLlantas(self) -> None:
        self._llantas = []  # se asigna a self._llantas una lista
        for _ in range(4):
            self._llantas.append(
                Producto(
                    TipoProducto.LLANTA, Carro.inicializarEstado(), self.getMarca()
                )
            )

    # metodo que crea cuatro Productos tipo Rin y los agrega a self._rines
    def _inicializarRines(self) -> None:
        self._rines = []  # se asigna a self._rines una lista
        for _ in range(4):
            self._rines.append(
                Producto(TipoProducto.RIN, Carro.inicializarEstado(), self.getMarca())
            )

    # metodo que crea los depositos y los asigna a self._depositos
    def _inicializarDepositos(self) -> None:
        self._depositos = []
        self._depositos.append(
            Producto(TipoProducto.GASOLINA, Carro.inicializarEstado(), self.getMarca())
        )
        self._depositos.append(
            Producto(TipoProducto.ACEITE, Carro.inicializarEstado(), self.getMarca())
        )
        self._depositos.append(
            Producto(TipoProducto.LIQUIDOS, Carro.inicializarEstado(), self.getMarca())
        )

    # metodo para asignar un solo producto
    def _inicializarProducto(self, tipo: TipoProducto) -> Producto:
        return Producto(tipo, Carro.inicializarEstado(), self.getMarca())

    # metodo para crear los amortiguadores
    def _inicializarAmortiguadores(self) -> None:
        self._amortiguadores = []
        for _ in range(4):
            self._amortiguadores.append(
                Producto(
                    TipoProducto.AMORTIGUADOR,
                    Carro.inicializarEstado(),
                    self.getMarca(),
                )
            )

    # metodo para generar el estado de manera randomizada
    @staticmethod
    def inicializarEstado() -> TipoEstado:
        numero = random.randint(0, 2)
        return TipoEstado.segunNumero(numero)
