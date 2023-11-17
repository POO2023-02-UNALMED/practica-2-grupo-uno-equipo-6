import tkinter as tk
from typing import Any, cast
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.parqueadero.plaza import Plaza
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame
from admon_parqueadero.uiMain.componentes.formulario_cliente import FormularioCliente
from admon_parqueadero.uiMain.componentes.formulario_vehiculo import FormularioVehiculo
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad


class IngresarVehiculo(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.frame_botones: tk.Frame

        self.setTitulo("Ingresar Vehículo")
        self.setDescripcion(
            "Bienvenido, aquí podrá ingresar vehículos al parqueadero.\
 Para comenzar, escriba su documento de identidad.\
 En caso de no estar registrado, ingrese los datos personales y del vehículo que se solicitan.\
 Al finalizar, se generará automaticamente la factura con hora de ingreso."
        )

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

        formulario = FormularioVehiculo(
            self.contenido,
            self.getBaseDatos(),
            cliente,
            f_final=self._configurar_ingreso,
        )
        formulario.pack()

    def _configurar_ingreso(self, vehiculo: Vehiculo):
        if vehiculo.estaParqueado():
            tk.Label(self.contenido, text="Ese vehículo ya se encuentra ingresado en el parqueadero").pack()
            tk.Button(self.contenido, text="Regresar", command=lambda: self._configurar_ui(vehiculo.getDueno())).pack()
            return

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

        self.field_frame.destroy()
        self.frame_botones.destroy()

        tk.Label(self.contenido, text="Vehículo ingresado").pack()

