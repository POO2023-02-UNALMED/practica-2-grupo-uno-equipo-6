import random
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
        dueno: Cliente,
        marca: str,
        color: str,
        modelo: str,
        tipo: TipoVehiculo,
        puestos: int,
        discapacitado: bool,
        precioVenta: float | None = None,
    ):
        super().__init__(placa, dueno, marca, color, modelo)
        self.tipo = tipo
        self.puestos = puestos
        self.motor = self.inicializarProducto(TipoProducto.MOTOR)
        self.transmision = self.inicializarProducto(TipoProducto.TRANSMISION)
        self.acelerador = self.inicializarProducto(TipoProducto.ACELERADOR)
        self.freno = self.inicializarProducto(TipoProducto.FRENO)
        self.bateria = self.inicializarProducto(TipoProducto.BATERIA)
        self.pedal = self.inicializarProducto(TipoProducto.PEDAL)
        self.inicializarDepositos()
        self.inicializarLlantas()
        self.inicializarRines()
        self.inicializarAmortiguadores()
        self.precioVenta = 0.0
        self.discapacitado = discapacitado

        if precioVenta is not None:
            self.precioVenta = precioVenta
            self.motor.setEstado(TipoEstado.EXCELENTE_ESTADO)
            self.acelerador.setEstado(TipoEstado.EXCELENTE_ESTADO)
            self.freno.setEstado(TipoEstado.EXCELENTE_ESTADO)
            self.bateria.setEstado(TipoEstado.EXCELENTE_ESTADO)
            self.pedal.setEstado(TipoEstado.EXCELENTE_ESTADO)
            self.transmision.setEstado(TipoEstado.EXCELENTE_ESTADO)
            for p in self.depositos:
                p.setEstado(TipoEstado.EXCELENTE_ESTADO)
            for p in self.llantas:
                p.setEstado(TipoEstado.EXCELENTE_ESTADO)
            for p in self.rines:
                p.setEstado(TipoEstado.EXCELENTE_ESTADO)
            for p in self.amortiguadores:
                p.setEstado(TipoEstado.EXCELENTE_ESTADO)

    def isDiscapacitado(self) -> bool:
        return self.discapacitado

    def setDiscapacitado(self, discapacitado: bool) -> None:
        self.discapacitado = discapacitado

    def getPrecioVenta(self) -> float:
        return self.precioVenta

    def setPrecioVenta(self, precioVenta: float) -> None:
        self.precioVenta = precioVenta

    def getTipo(self) -> str:
        return self.tipo.name

    def setTipo(self, tipo: TipoVehiculo) -> None:
        self.tipo = tipo

    def getPuestos(self) -> int:
        return self.puestos

    def setPuestos(self, puestos: int) -> None:
        self.puestos = puestos

    def getMotor(self) -> Producto:
        return self.motor

    def setMotor(self, motor: Producto) -> None:
        self.motor = motor

    def getTransmision(self) -> Producto:
        return self.transmision

    def setTransmision(self, transmision: Producto) -> None:
        self.transmision = transmision

    def getAcelerador(self) -> Producto:
        return self.acelerador

    def setAcelerador(self, acelerador: Producto) -> None:
        self.acelerador = acelerador

    def getFreno(self) -> Producto:
        return self.freno

    def setFreno(self, freno: Producto) -> None:
        self.freno = freno

    def getBateria(self) -> Producto:
        return self.bateria

    def setBateria(self, bateria: Producto) -> None:
        self.bateria = bateria

    def getPedal(self) -> Producto:
        return self.pedal

    def setPedal(self, pedal: Producto) -> None:
        self.pedal = pedal

    def getDepositos(self) -> list[Producto]:
        return self.depositos

    def setDepositos(self, depositos: list[Producto]) -> None:
        self.depositos = depositos

    def getLlantas(self) -> list[Producto]:
        return self.llantas

    def setLlantas(self, llantas: list[Producto]) -> None:
        self.llantas = llantas

    def getRines(self) -> list[Producto]:
        return self.rines

    def setRines(self, rines: list[Producto]) -> None:
        self.rines = rines

    def getAmortiguadores(self) -> list[Producto]:
        return self.amortiguadores

    def setAmortiguadores(self, amortiguadores: list[Producto]) -> None:
        self.amortiguadores = amortiguadores

    def __str__(self) -> str:
        marca = self.getMarca().title()
        modelo = self.getModelo().title()
        color = self.getColor().title()
        tipo = self.getTipo().title()
        puestos = self.getPuestos()
        if self.precioVenta != 0:  # para los carros para venta se imprime su valor
            precioVenta = round(self.getPrecioVenta(), 2)
            return f"{marca} {modelo} {color}\n{tipo} {puestos} puestos\nPrecio: {precioVenta}"
        return f"{marca} {modelo} {color}\n{tipo} {puestos} puestos\n"

    # metodo que crea cuatro Productos tipo llanta y los agrega al array self.llantas
    def inicializarLlantas(self) -> None:
        self.llantas = []  # se asigna a self.llantas una lista
        for _ in range(4):
            self.llantas.append(
                Producto(
                    TipoProducto.LLANTA, self.getMarca(), Carro.inicializarEstado()
                )
            )

    # metodo que crea cuatro Productos tipo Rin y los agrega a self.rines
    def inicializarRines(self) -> None:
        self.rines = []  # se asigna a self.rines una lista
        for _ in range(4):
            self.rines.append(
                Producto(TipoProducto.RIN, self.getMarca(), Carro.inicializarEstado())
            )

    # metodo que crea los depositos y los asigna a self.depositos
    def inicializarDepositos(self) -> None:
        self.depositos = []
        self.depositos.append(
            Producto(TipoProducto.GASOLINA, self.getMarca(), Carro.inicializarEstado())
        )
        self.depositos.append(
            Producto(TipoProducto.ACEITE, self.getMarca(), Carro.inicializarEstado())
        )
        self.depositos.append(
            Producto(TipoProducto.LIQUIDOS, self.getMarca(), Carro.inicializarEstado())
        )

    # metodo para asignar un solo producto
    def inicializarProducto(self, tipo: TipoProducto) -> Producto:
        return Producto(tipo, self.getMarca(), Carro.inicializarEstado())

    # metodo para crear los amortiguadores
    def inicializarAmortiguadores(self) -> None:
        self.amortiguadores = []
        for _ in range(4):
            self.amortiguadores.append(
                Producto(
                    TipoProducto.AMORTIGUADOR,
                    self.getMarca(),
                    Carro.inicializarEstado(),
                )
            )

    # metodo para generar el estado de manera randomizada
    @staticmethod
    def inicializarEstado() -> TipoEstado:
        numero = random.randint(0, 2)
        return TipoEstado.segunNumero(numero)
