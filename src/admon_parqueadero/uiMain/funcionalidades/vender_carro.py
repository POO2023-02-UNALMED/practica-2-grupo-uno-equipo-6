import tkinter as tk
from typing import Any, cast
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad
from admon_parqueadero.uiMain.componentes.formulario_cliente import FormularioCliente
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame
from admon_parqueadero.uiMain.componentes.formulario_carro import FormularioCarro
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo
from admon_parqueadero.gestorAplicacion.parqueadero.plaza import Plaza
from admon_parqueadero.gestorAplicacion.parqueadero.parqueadero import Parqueadero



class VenderCarro(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.setTitulo("Vender Carro")
        self.setDescripcion("Bienvenido, aquí podrá vender un carro, o intercambiarlo por uno de los que\
 se encuentran disponibles en el parqueadero. Para comenzar, ingrese su cédula,\
 en caso de no estar registrado se solicita rellenar sus datos y generar el ingreso \
 al parqueadero del vehículo que desea vender.")
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        formulario = FormularioCliente(
            self.contenido, self.getBaseDatos(), f_final=self._configurar_ui
        )
        formulario.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)
    def _configurar_ui(self, cliente: Cliente) -> None:
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        formulario = FormularioCarro(
            self.contenido,
            self.getBaseDatos(),
            cliente,
            f_final=self._configurar_ingreso,
        )
        formulario.pack()
    def _configurar_ingreso(self, vehiculo: Vehiculo):
        if vehiculo.estaParqueado():
            self.imprimir("Ese vehículo ya se encuentra ingresado en el parqueadero")
            return self._configurar_ui(vehiculo.getDueno())

        plazas_disponibles = map(
            lambda p: str(p.getNumeroPlaza()),
            self.getParqueadero().plazasDisponiblesPara(vehiculo),
        )
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterios",
            ["Cédula", "Placa", "Plaza"],
            "Valores",
            [str(vehiculo.getDueno().getCedula()), vehiculo.getPlaca(), None],
            ["Cédula", "Placa"],
            combobox={"Plaza": list(plazas_disponibles)},
        )
        self.field_frame.pack()

        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)

        self.btn_principal = tk.Button(
            self.frame_botones, text="Ingresar", command=self._terminar_ingreso
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=self.field_frame.borrar
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def _terminar_ingreso(self):
        placa = self.field_frame.getValue("Placa")
        plaza_num = int(self.field_frame.getValue("Plaza"))
        vehiculo = cast(Vehiculo, self.getBaseDatos().buscarVehiculoRegistrado(placa))
        plaza = cast(Plaza, self.getParqueadero().buscarPlaza(plaza_num))
        self.getParqueadero().ingresarVehiculo(vehiculo, plaza)

        # TODO: Generar factura

        self.imprimir("Vehículo ingresado")
        self._configurar_ui(vehiculo.getDueno())
    
    #Mostrar lista de vendedores disponibles
    def escoger_vendedor(self):
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        vendedores = []
        for empleado in Parqueadero.getEmpleados():
            if empleado.getCargo() == "vendedor":
                vendedores.append(empleado)
        
        self.field_frame = FieldFrame(
            self,
            "Criterio",
            ["Escoja al vendedor de su preferencia"],
            "Valor",
            combobox={
                "Escoja al vendedor de su preferencia": vendedores
            },
        )



