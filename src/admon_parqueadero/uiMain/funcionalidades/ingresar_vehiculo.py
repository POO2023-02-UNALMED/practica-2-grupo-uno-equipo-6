#Funcionalidad del módulo: contiene la clase IngresarVehiculo, que hereda de BaseFuncionalidad,
#Aquí se encuentra la implementación de la funcionalidad ingresar vehículo.
#Inicia solicitando los datos del cliente, en caso de que no se encuentre registrado,
#se pide registrarse, se pide informacion del vehículo y se genera la factura de ingreso.
#Componentes del módulo: IngresarVehiculo
#Autores: Alejandro, Sebastián


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
            self.contenido, self.getBaseDatos(), f_final=self._configurar_ui, imprimir=self.imprimir
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
            imprimir=self.imprimir
        )
        formulario.pack()

    def _configurar_ingreso(self, vehiculo: Vehiculo):
        dueno = vehiculo.getDueno()
        if dueno is not None:
            if vehiculo.estaParqueado():
                self.imprimir("Ese vehículo ya se encuentra ingresado en el parqueadero")
                return self._configurar_ui(dueno)

            plazas_disponibles = map(
                lambda p: str(p.getNumeroPlaza()),
                self.getParqueadero().plazasDisponiblesPara(vehiculo),
            )
            self.field_frame = FieldFrame(
                self.contenido,
                "Criterios",
                ["Cédula", "Placa", "Plaza"],
                "Valores",
                [str(dueno.getCedula()), vehiculo.getPlaca(), None],
                ["Cédula", "Placa"],
                combobox={"Plaza": list(plazas_disponibles)},
                titulo="Seleccione una plaza"
            )
            self.field_frame.pack()

            self.frame_botones = tk.Frame(self.contenido)
            self.frame_botones.pack(side="bottom", fill="both", expand=True)

            self.btn_principal = tk.Button(
                self.frame_botones, text="Ingresar", command=self._terminar_ingreso
            )
            self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

            self.btn_borrar = tk.Button(
                self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
            )
            self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def _terminar_ingreso(self):
        placa = self.field_frame.getValue("Placa")
        plaza_num = int(self.field_frame.getValue("Plaza"))
        vehiculo = cast(Vehiculo, self.getBaseDatos().buscarVehiculoRegistrado(placa))
        plaza = cast(Plaza, self.getParqueadero().buscarPlaza(plaza_num))
        self.getParqueadero().ingresarVehiculo(vehiculo, plaza)
        dueno = vehiculo.getDueno()

        self.imprimir("Vehículo ingresado")
        
        if dueno is not None:
            self._configurar_ui(dueno)

