from admon_parqueadero.gestorAplicacion.personas.persona import Persona
from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_estado import TipoEstado
from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto
from admon_parqueadero.gestorAplicacion.vehiculos.carro import Carro
from admon_parqueadero.gestorAplicacion.vehiculos.moto import Moto
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo


class Empleado(Persona):
    def __init__(
        self,
        nombre: str,
        cedula: int,
        telefono: int,
        correo: str,
        direccion: str,
        cargo: str,
        salario: float,
    ) -> None:
        super().__init__(nombre, cedula, telefono, correo, direccion)
        self._cargo = cargo
        self._salario = salario
        self._comision = 0.1
        self._serviciosRealizados = 0

    def setCargo(self, cargo: str) -> None:
        self._cargo = cargo

    def getCargo(self) -> str:
        return self._cargo

    def setSalario(self, salario: float) -> None:
        self._salario = salario

    def getSalario(self) -> float:
        return self._salario

    def setComision(self, comision: float) -> None:
        self._comision = comision

    def getComision(self) -> float:
        return self._comision

    def setServiciosRealizados(self, serviciosRealizados: int) -> None:
        self._serviciosRealizados = serviciosRealizados

    def getServiciosRealizados(self) -> int:
        return self._serviciosRealizados

    # Metodo que utiliza un empleado de tipo mecanico para revisar un vehiculo y devolver su estado
    def revisarVehiculo(self, vehiculo: Vehiculo) -> list[Producto]:
        r: list[Producto] = []

        if self.getCargo() == "Mecanico":
            if isinstance(vehiculo, Carro):
                if vehiculo.getMotor().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getMotor())

                if vehiculo.getTransmision().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getTransmision())

                if vehiculo.getAcelerador().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getAcelerador())

                if vehiculo.getFreno().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getFreno())

                if vehiculo.getBateria().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getBateria())

                if vehiculo.getPedal().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getPedal())

                for p in vehiculo.getDepositos():
                    if p.getEstado() == TipoEstado.MAL_ESTADO:
                        r.append(p)

                for p in vehiculo.getLlantas():
                    if p.getEstado() == TipoEstado.MAL_ESTADO:
                        r.append(p)

                for p in vehiculo.getRines():
                    if p.getEstado() == TipoEstado.MAL_ESTADO:
                        r.append(p)

                for p in vehiculo.getAmortiguadores():
                    if p.getEstado() == TipoEstado.MAL_ESTADO:
                        r.append(p)

            if isinstance(vehiculo, Moto):
                if vehiculo.getMotor().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getMotor())

                if vehiculo.getTransmision().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getTransmision())

                if vehiculo.getAcelerador().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getAcelerador())

                if vehiculo.getFreno().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getFreno())

                if vehiculo.getCadena().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getCadena())

                if vehiculo.getPedales().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getPedales())

                if vehiculo.getBateria().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getBateria())

                if vehiculo.getAmortiguador().getEstado() == TipoEstado.MAL_ESTADO:
                    r.append(vehiculo.getAmortiguador())

                for p in vehiculo.getDepositos():
                    if p.getEstado() == TipoEstado.MAL_ESTADO:
                        r.append(p)

                for p in vehiculo.getLlantas():
                    if p.getEstado() == TipoEstado.MAL_ESTADO:
                        r.append(p)

                for p in vehiculo.getRines():
                    if p.getEstado() == TipoEstado.MAL_ESTADO:
                        r.append(p)

            return r

        return r

    # Metodo para cambiar un componente de un vehiculo por otro
    def cambiar(
        self, productoViejo: Producto, productoNuevo: Producto, vehiculo: Vehiculo
    ) -> None:
        productoNuevo.setMarca(vehiculo.getMarca())
        productoNuevo.setPrecio(0)

        if isinstance(vehiculo, Carro):
            if vehiculo.getMotor() == productoViejo:
                vehiculo.setMotor(productoNuevo)

            if vehiculo.getTransmision() == productoViejo:
                vehiculo.setTransmision(productoNuevo)

            if vehiculo.getAcelerador() == productoViejo:
                vehiculo.setAcelerador(productoNuevo)

            if vehiculo.getFreno() == productoViejo:
                vehiculo.setFreno(productoNuevo)

            if vehiculo.getBateria() == productoViejo:
                vehiculo.setBateria(productoNuevo)

            if vehiculo.getPedal() == productoViejo:
                vehiculo.setPedal(productoNuevo)

            i = 0
            for p in vehiculo.getDepositos():
                if p == productoViejo:
                    vehiculo.getDepositos()[i] = productoNuevo
                    i = 0
                    return
                i += 1

            i = 0

            for p in vehiculo.getLlantas():
                if p == productoViejo:
                    vehiculo.getLlantas()[i] = productoNuevo
                    i = 0
                    return
                i += 1

            i = 0

            for p in vehiculo.getRines():
                if p == productoViejo:
                    vehiculo.getRines()[i] = productoNuevo
                    i = 0
                    return
                i += 1

            i = 0

            for p in vehiculo.getAmortiguadores():
                if p == productoViejo:
                    vehiculo.getAmortiguadores()[i] = productoNuevo
                    i = 0
                    return
                i += 1

            i = 0

        if isinstance(vehiculo, Moto):
            if vehiculo.getMotor() == productoViejo:
                vehiculo.setMotor(productoNuevo)

            if vehiculo.getTransmision() == productoViejo:
                vehiculo.setTransmision(productoNuevo)

            if vehiculo.getAcelerador() == productoViejo:
                vehiculo.setAcelerador(productoNuevo)

            if vehiculo.getFreno() == productoViejo:
                vehiculo.setFreno(productoNuevo)

            if vehiculo.getCadena() == productoViejo:
                vehiculo.setCadena(productoNuevo)

            if vehiculo.getPedales() == productoViejo:
                vehiculo.setPedales(productoNuevo)

            if vehiculo.getBateria() == productoViejo:
                vehiculo.setBateria(productoNuevo)

            if vehiculo.getAmortiguador() == productoViejo:
                vehiculo.setAmortiguador(productoNuevo)

            i = 0
            for p in vehiculo.getDepositos():
                if p == productoViejo:
                    vehiculo.getDepositos()[i] = productoNuevo
                    i = 0
                    return
                i += 1

            i = 0
            for p in vehiculo.getLlantas():
                if p == productoViejo:
                    vehiculo.getLlantas()[i] = productoNuevo
                    i = 0
                    return
                i += 1

            i = 0
            for p in vehiculo.getRines():
                if p == productoViejo:
                    vehiculo.getRines()[i] = productoNuevo
                    i = 0
                    return
                i += 1
