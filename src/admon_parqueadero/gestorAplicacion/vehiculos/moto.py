import random
from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_estado import TipoEstado
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_producto import TipoProducto
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.gestorAplicacion.vehiculos.tipo_vehiculo import TipoVehiculo
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(
        self,
        placa: str,
        dueno: Cliente,
        marca: str,
        color: str,
        modelo: str,
        tipo: TipoVehiculo,
        cilindraje: int,
    ) -> None:
        super().__init__(placa, dueno, marca, color, modelo)
        self._tipo = tipo
        self._cilindraje = cilindraje
        self._motor = self.inicializarProducto(TipoProducto.MOTOR)
        self._transmision = self.inicializarProducto(TipoProducto.TRANSMISION)
        self._acelerador = self.inicializarProducto(TipoProducto.ACELERADOR)
        self._freno = self.inicializarProducto(TipoProducto.FRENO)
        self._cadena = self.inicializarProducto(TipoProducto.CADENA)
        self._pedales = self.inicializarProducto(TipoProducto.PEDALES)
        self._bateria = self.inicializarProducto(TipoProducto.BATERIA)
        self._amortiguador = self.inicializarProducto(TipoProducto.AMORTIGUADOR)
        self.inicializarDepositos()
        self.inicializarLlantas()
        self.inicializarRines()

    def getTipo(self) -> TipoVehiculo:
        return self._tipo

    def setTipo(self, tipo: TipoVehiculo) -> None:
        self._tipo = tipo

    def getLlantas(self) -> list[Producto]:
        return self._llantas

    def setLlantas(self, llantas: list[Producto]) -> None:
        self._llantas = llantas

    def getCilindraje(self) -> int:
        return self._cilindraje

    def setCilindraje(self, cilindraje: int) -> None:
        self._cilindraje = cilindraje

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

    def getCadena(self) -> Producto:
        return self._cadena

    def setCadena(self, cadena: Producto) -> None:
        self._cadena = cadena

    def getPedales(self) -> Producto:
        return self._pedales

    def setPedales(self, pedales: Producto) -> None:
        self._pedales = pedales

    def getDepositos(self) -> list[Producto]:
        return self._depositos

    def setDepositos(self, depositos: list[Producto]) -> None:
        self._depositos = depositos

    def getRines(self) -> list[Producto]:
        return self._rines

    def setRines(self, rines: list[Producto]) -> None:
        self._rines = rines

    def getBateria(self) -> Producto:
        return self._bateria

    def setBateria(self, bateria: Producto) -> None:
        self._bateria = bateria

    def getAmortiguador(self) -> Producto:
        return self._amortiguador

    def setAmortiguador(self, amortiguador: Producto) -> None:
        self._amortiguador = amortiguador

    # metodo que crea dos Productos tipo llanta y los agrega al array self._llantas
    def inicializarLlantas(self) -> None:
        self._llantas = []  # se asigna a self._llantas una lista
        for _ in range(2):
            self._llantas.append(
                Producto(TipoProducto.LLANTA, Moto.inicializarEstado(), self.getMarca())
            )

    # metodo que crea dos Productos tipo Rin y los agrega a self._rines
    def inicializarRines(self) -> None:
        self._rines = []  # se asigna a self._rines una lista
        for _ in range(2):
            self._rines.append(
                Producto(TipoProducto.RIN, Moto.inicializarEstado(), self.getMarca())
            )

    # metodo que crea los depositos y los asigna a self._depositos
    def inicializarDepositos(self) -> None:
        self._depositos = []
        self._depositos.append(
            Producto(TipoProducto.GASOLINA, Moto.inicializarEstado(), self.getMarca())
        )
        self._depositos.append(
            Producto(TipoProducto.ACEITE, Moto.inicializarEstado(), self.getMarca())
        )
        self._depositos.append(
            Producto(TipoProducto.LIQUIDOS, Moto.inicializarEstado(), self.getMarca())
        )

    # metodo para asignar un solo producto
    def inicializarProducto(self, tipo: TipoProducto) -> Producto:
        return Producto(tipo, Moto.inicializarEstado(), self.getMarca())

    @classmethod
    def inicializarEstado(cls) -> TipoEstado:
        numero = random.randint(0, 2)
        return TipoEstado.segunNumero(numero)
