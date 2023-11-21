from __future__ import annotations

from datetime import date, time, datetime
from typing import TYPE_CHECKING
from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto

if TYPE_CHECKING:
    from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente


class Factura:
    _facturasCreadas = 0

    def __init__(self, cliente: Cliente) -> None:
        Factura._facturasCreadas += 1
        self._numeroFactura = Factura._facturasCreadas
        self._fecha = datetime.now().date()
        self._horaIngreso = datetime.now().time()
        self._cliente = cliente
        cliente.setFactura(self)
        self._precioTotal = 0
        self._servicios: dict[str, float] = {}
        self._valorServicios: dict[str, float] = {"Revision general": 100000, "Cambio": 50000, "Parqueadero": 1}

    def getNumeroFactura(self) -> int:
        return self._numeroFactura

    def setNumeroFactura(self, numeroFactura: int) -> None:
        self._numeroFactura = numeroFactura

    def getFecha(self) -> date:
        return self._fecha

    def setFecha(self, fecha: date) -> None:
        self._fecha = fecha

    def getHoraIngreso(self) -> time:
        return self._horaIngreso

    def setHoraIngreso(self, horaIngreso: time) -> None:
        self._horaIngreso = horaIngreso

    def getPrecioTotal(self) -> float:
        return self._precioTotal

    def setPrecioTotal(self, precioTotal: int) -> None:
        self._precioTotal = precioTotal

    def getCliente(self) -> Cliente:
        return self._cliente

    def setCliente(self, cliente: Cliente) -> None:
        self._cliente = cliente

    def getServicios(self) -> dict[str, float]:
        return self._servicios

    def setServicios(self, servicios: dict[str, float]) -> None:
        self._servicios = servicios

    @classmethod
    def getFacturasCreadas(cls) -> int:
        return Factura._facturasCreadas

    @classmethod
    def setFacturasCreadas(cls, facturasCreadas: int) -> None:
        Factura._facturasCreadas = facturasCreadas

    @classmethod
    def getValorServicios(cls) -> dict[str, float]:
        return Factura._valorServicios

    @classmethod
    def setValorServicios(cls, valorServicios: dict[str, float]) -> None:
        Factura._valorServicios = valorServicios

    def agregarProducto(self, producto: Producto, cantidad: float) -> None:
        key = f"Compra de {producto.getTipo().name.capitalize()}s"
        if key in self._valorServicios:
            self._servicios[key] += cantidad
        else:
            self._servicios[key] = cantidad

    def agregarServicio(self, servicio: str, cantidad: float) -> None:
        if servicio in self._servicios:
            if servicio.split(" ")[0] == "Cambio":
                self._servicios[servicio] += cantidad * self._valorServicios["Cambio"]
            else:
                self._servicios[servicio] += cantidad * self._valorServicios[servicio]
        else:
            if servicio.split(" ")[0] == "Cambio":
                self._servicios[servicio] = cantidad * self._valorServicios["Cambio"]
            else:
                self._servicios[servicio] = cantidad * self._valorServicios[servicio]

    def __str__(self) -> str:
        servicios = ""
        for key in self._servicios:
            servicios += f"{key}: {self._servicios.get(key)}\n"
        s = f"Factura N°{self._numeroFactura}        {self._fecha.strftime('%Y/%m/%d')}\nCliente: {self._cliente.getNombre()}\n"
        if len(servicios) > 0:
            s += f"Servicios:\n{servicios}"
        return s
