import tkinter as tk
from typing import Any, Callable
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame
from admon_parqueadero.uiMain.componentes.formulario_cliente import FormularioCliente

from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad


class IngresarVehiculo(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.frame_botones: tk.Frame

        self.setTitulo("Ingresar Vehículo")
        self.setDescripcion("Bienvenido, aquí podrá ingresar vehículos al parqueadero.\
                    Para comenzar, escriba su documento de identidad.\
                    En caso de no estar registrado, ingrese los datos personales y del vehículo que se solicitan.\
                     Al finalizar, se generará automaticamente la factura con hora de ingreso.")

        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        formulario = FormularioCliente(
            self.contenido, self.getBaseDatos(), f_final=self._configurar_ui
        )
        formulario.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)

    def _configurar_ui(self, cliente: Cliente) -> None:
        placas_vehiculos = map(lambda v: v.getPlaca(), cliente.getVehiculos())

        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Cédula", "Vehículo a ingresar"],
            "Valor",
            [str(cliente.getCedula()), None],
            ["Cédula"],
            combobox={
                "Vehículo a ingresar": [*placas_vehiculos, "Registrar un vehículo"]
            },
        )
        self.field_frame.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)
        self._generar_botones("Continuar", lambda: self._continuar_inicio(cliente))

    def _continuar_inicio(self, cliente: Cliente) -> None:
        eleccion_vehiculo = self.field_frame.getValue("Vehículo a ingresar")
        if eleccion_vehiculo == "Registrar un vehículo":
            self._registro_vehiculo(cliente)
        else:
            pass

    def _registro_vehiculo(self, cliente: Cliente) -> None:
        self.field_frame.destroy()
        self.frame_botones.destroy()

        tiposVehiculo = ["Carro"]
        if not cliente.isDiscapacitado():
            tiposVehiculo.append("Moto")

        coloresVehiculo = [
            "Rojo",
            "Azul",
            "Verde",
            "Morado",
            "Naranja",
            "Gris",
            "Negro",
            "Blanco",
            "Rosado",
            "Amarillo",
        ]

        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Cédula", "Placa", "Tipo", "Color", "Modelo"],
            "Valores",
            [str(cliente.getCedula()), None, None, None, None],
            ["Cédula"],
            combobox={"Tipo": tiposVehiculo, "Color": coloresVehiculo},
            titulo="Registro de vehiculo",
        )
        self.field_frame.pack()

        self._generar_botones("Continuar", lambda: self._continuar_registro())

    def _continuar_registro(self) -> None:
        pass

    def _generar_botones(
        self,
        text_principal: str,
        f_principal: Callable[[], None],
    ) -> None:
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)

        tk.Button(self.frame_botones, text=text_principal, command=f_principal).pack(
            side="left", fill="both", expand=True, padx=15
        )
        tk.Button(
            self.frame_botones, text="Borrar", command=self.field_frame.borrar
        ).pack(side="right", fill="both", expand=True, padx=15)
