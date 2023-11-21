from time import sleep
import tkinter as tk
 
from typing import Any, cast, Literal
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.errores import ErrorObjetoVacio
from admon_parqueadero.gestorAplicacion.vehiculos.carro import Carro
from admon_parqueadero.gestorAplicacion.vehiculos.coloresVehiculo import ColoresVehiculo
from admon_parqueadero.gestorAplicacion.vehiculos.marcasCarro import MarcasCarro
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad
from admon_parqueadero.gestorAplicacion.personas.empleado import Empleado
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame

from admon_parqueadero.uiMain.componentes.formulario_cliente import FormularioCliente


class ComprarCarro(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.setTitulo("Comprar Carro")
        self.setDescripcion("""Bienvenido, aquí podrá comprar un carro según sus preferencias.
        Para comenzar, ingrese su documento, en caso de no estar registrado,
        ingrese sus datos""")
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        formulario = FormularioCliente(
            self.contenido, self.getBaseDatos(), f_final=self._configurar_ui, imprimir=self.imprimir
        )
        formulario.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)

    def _configurar_ui(self, cliente: Cliente) -> None:
        self.cliente = cliente
        self.nombreCliente = cliente.getNombre()
        self._vendedores_nombre = list(
            map(lambda x: x.getNombre().title(), self._parqueadero.getVendedores())
        )
        
        self._vehiculos_color = list(
            map(lambda x: x.getColor().title(), self._parqueadero.getVehiculosVenta())
        )
        
        self._vehiculos_marca = list(
            map(lambda x: x.getMarca().title(), self._parqueadero.getVehiculosVenta())
        )
        
        self.EscogerVendedor()
    def EscogerVendedor (self):
        self.vendedorSelected = None
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        
        # mensaje de bienvenida
        
        mensajeBienvenida = f"""Bienvenido de nuevo, {self.nombreCliente}
        Seleccione al vendedor de su preferencia"""
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Vendedor"],
            "Valor",
            None,
            None,
            {"Vendedor": self._vendedores_nombre},
            mensajeBienvenida
        )
        self.field_frame.pack()
        
        
        
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        
        self.btn_principal = tk.Button(
            self.frame_botones, text="Continuar", command=lambda: self.pregunta_filtro()
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def pregunta_filtro(self) -> None:
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        self.field_frame = FieldFrame(self.contenido, "Criterio", ["Filtro"], "Valor", None, None, {"Filtro": ["Color", "Marca", "Precio máximo"]}, titulo="Seleccione por que criterio quiere buscar su vehiculo")
        self.field_frame.pack()
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        
        self.btn_principal = tk.Button(
            self.frame_botones, text="Continuar", command=lambda: self.eleccion_filtro()
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def eleccion_filtro(self) -> None:
        criterio = self.field_frame.getValue("Filtro")
        if criterio == "Color":
            return self.EscogerVehiculo("Color")
        elif criterio == "Marca":
            return self.EscogerVehiculo("Marca")
        else:
            return self.EscogerVehiculo("Precio")
            
    def EscogerVehiculo(self, criterio: Literal["Color", "Marca", "Precio"]) -> None:
        self.field_frame.destroy()
        if criterio == "Marca":
            self.field_frame = FieldFrame(self.contenido, "Criterio", ["Marca"], "Valor", None, None, {"Marca": [m.name.title() for m in MarcasCarro]}, titulo="Seleccione una marca")
            self.field_frame.pack()
            self.btn_principal.config(command=lambda: self.eleccion_marca())
        elif criterio == "Color":
            self.field_frame = FieldFrame(self.contenido, "Criterio", ["Color"], "Valor", None, None, {"Color": ColoresVehiculo.lista()}, titulo="Seleccione un color")
            self.field_frame.pack()
            self.btn_principal.config(command=lambda: self.eleccion_color())
        else:
            self.field_frame = FieldFrame(self.contenido, "Criterio", ["Precio máximo"], "Valor", None, None, titulo="Ingrese el precio máximo")
            self.field_frame.pack()
            self.btn_principal.config(command=lambda: self.eleccion_precio())


    def eleccion_marca(self):
        marca = self.field_frame.getValue("Marca")
        self.vehiculos = filter(lambda v: v.getMarca().upper() == marca.upper(), self._parqueadero.getVehiculosVenta())
        if self.cliente.isDiscapacitado():
            self.vehiculos = filter(lambda v: v.isDiscapacitado(), self.vehiculos)
        self.vehiculos = list(self.vehiculos)
        if len(self.vehiculos) == 0:
            try:
                raise ErrorObjetoVacio("No se encontraron carros con las caracteristicas especificadas")
            finally:
                return self.pregunta_filtro()
        self.placas = map(lambda p: p.getPlaca(), self.vehiculos)
        self.field_frame.destroy()
        self.field_frame = FieldFrame(self.contenido, "Criterio", ["Placa"], "Valor", None, None, {"Placa": list(self.placas)}, titulo= "Seleccione la placa del vehiculo gustado")
        self.field_frame.pack()
        self.btn_principal.config(command= lambda: self.seleccionar_carro())
        for vehiculo in self.vehiculos:
            self.imprimir(str(vehiculo))
            self.imprimir()

    def eleccion_color(self) -> None:
        color = self.field_frame.getValue("Color")
        self.vehiculos = filter(lambda v: v.getColor() == color, self._parqueadero.getVehiculosVenta())
        if self.cliente.isDiscapacitado():
            self.vehiculos = filter(lambda v: v.isDiscapacitado(), self.vehiculos)
        self.vehiculos = list(self.vehiculos)
        if len(self.vehiculos) == 0:
            try:
                raise ErrorObjetoVacio("No se encontraron carros con las caracteristicas especificadas")
            finally:
                return self.pregunta_filtro()
        self.placas = map(lambda v: v.getPlaca(), self.vehiculos)
        self.field_frame.destroy()
        self.field_frame = FieldFrame(self.contenido, "Criterio", ["Placa"], "Valor", None, None, {"Placa": [*self.placas]}, titulo= "Seleccione la placa del vehiculo gustado")
        self.field_frame.pack()
        self.btn_principal.config(command= lambda: self.seleccionar_carro())
        for vehiculo in self.vehiculos:
            self.imprimir(str(vehiculo))
            self.imprimir()

    def eleccion_precio(self) -> None:
        precio = self.field_frame.getValueNumero("Precio máximo", float)
        self.vehiculos = filter(lambda v: v.getPrecioVenta() <= precio, self._parqueadero.getVehiculosVenta())
        if self.cliente.isDiscapacitado():
            self.vehiculos = filter(lambda v: v.isDiscapacitado(), self.vehiculos)
        self.vehiculos = list(self.vehiculos)
        if len(self.vehiculos) == 0:
            try:
                raise ErrorObjetoVacio("No se encontraron carros con las caracteristicas especificadas")
            finally:
                return self.pregunta_filtro()
        self.placas = map(lambda v: v.getPlaca(), self.vehiculos)
        self.field_frame.destroy()
        self.field_frame = FieldFrame(self.contenido, "Criterio", ["Placa"], "Valor", None, None, {"Placa": [*self.placas]}, titulo= "Seleccione la placa del vehiculo gustado")
        self.field_frame.pack()
        self.btn_principal.config(command= lambda: self.seleccionar_carro())
        for vehiculo in self.vehiculos:
            self.imprimir(str(vehiculo))
            self.imprimir()
    
    def seleccionar_carro(self):
        self.seleccion_carro = self.field_frame.getValue("Placa")
        
        placas_carro_venta = map(lambda x: x.getPlaca().upper(), self._parqueadero.getVehiculosVenta())
        carroComprado = self._parqueadero.getVehiculosVenta()[[*placas_carro_venta].index(self.seleccion_carro)]
        
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["¿Desea comprar este carro?"],
            "Valor",
            None,
            habilitado=None,
            combobox={"¿Desea comprar este carro?": ["Sí", "No"]},
            titulo='Según las características enseñadas, ¿desea comprar este vehículo o seleccionar otro?'
        )
        self.field_frame.pack()
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        self.btn_principal = tk.Button(
            self.frame_botones, text="Continuar", command=lambda: self.finalizar_venta(carroComprado)
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)
        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def finalizar_venta(self, carro: Carro):
        seleccion = self.field_frame.getValue("¿Desea comprar este carro?")
        if seleccion == "No":
            return self.pregunta_filtro()

        carro.setDueno(self.cliente)
        carro.setPrecioVenta(0)
        self.cliente.getVehiculos().append(carro)
        indiceCarro = self._parqueadero.getVehiculosVenta().index(carro)
        self._parqueadero.getVehiculosVenta().pop(indiceCarro)
        self.imprimir("¡Felicidades! Ha comprado el carro, esperamos que lo disfrute. Vuelva pronto.")
        return self._configurar_ui(self.cliente)
