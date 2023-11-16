import logging
import tkinter as tk
from typing import Any, Callable

from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.gestorAplicacion.vehiculos.marcasMoto import MarcasMoto
from admon_parqueadero.gestorAplicacion.vehiculos.moto import Moto
from admon_parqueadero.gestorAplicacion.vehiculos.tipo_vehiculo import TipoVehiculo
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo
from admon_parqueadero.gestorAplicacion.vehiculos.carro import Carro
from admon_parqueadero.gestorAplicacion.vehiculos.marcasCarro import MarcasCarro
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame


class FormularioVehiculo(tk.Frame):
    def __init__(
        self,
        master: tk.Misc,
        baseDatos: BaseDatos,
        cliente: Cliente,
        f_final: Callable[[Vehiculo], None],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(master, *args, **kwargs)

        self._baseDatos = baseDatos
        self._cliente = cliente
        self._f_final = f_final

        self._configuracion_inicial()

    def _configuracion_inicial(self):
        placas_vehiculos = map(lambda v: v.getPlaca(), self._cliente.getVehiculos())

        self.field_frame = FieldFrame(
            self,
            "Criterio",
            ["Cédula", "Placa del vehículo"],
            "Valor",
            [str(self._cliente.getCedula()), None],
            ["Cédula"],
            combobox={
                "Vehículo a ingresar": [*placas_vehiculos, "Registrar un vehículo"]
            },
        )
        self.field_frame.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)

        self.frame_botones = tk.Frame(self)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)

        self.btn_principal = tk.Button(
            self.frame_botones, text="Continuar", command=self._continuar_inicio
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def _continuar_inicio(self) -> None:
        eleccion_vehiculo = self.field_frame.getValue("Placa del vehículo")
        if eleccion_vehiculo == "Registrar un vehículo":
            self._configuracion_registro()
        else:
            vehiculo = self._baseDatos.buscarVehiculoRegistrado(eleccion_vehiculo)
            self.destroy()
            self._f_final(vehiculo)

    def _configuracion_registro(self) -> None:
        self.field_frame.destroy()

        tiposVehiculo = ["Carro"]
        if not self._cliente.isDiscapacitado():
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
            self,
            "Criterio",
            ["Cédula", "Placa", "Tipo", "Color", "Modelo"],
            "Valores",
            [str(self._cliente.getCedula()), None, None, None, None],
            ["Cédula"],
            combobox={"Tipo": tiposVehiculo, "Color": coloresVehiculo},
            titulo="Registro de vehiculo",
        )
        self.field_frame.pack()

    def _continuar_registro(self) -> None:
        placa = self.field_frame.getValue("Placa")
        tipo = self.field_frame.getValue("Tipo")
        color = self.field_frame.getValue("Color")
        modelo = self.field_frame.getValue("Modelo")

        if self._baseDatos.buscarVehiculoRegistrado(placa) is not None:
            # TODO: Mostrar este error: vehiculo ya registrado
            # TODO: Considerar mover esto a baseDatos.registrarVehiculo o al contructor de Vehiculo
            logging.info(f"Vehiculo con placa {placa} ya registrado")
            return

        self.field_frame.destroy()

        anteriores_criterios = ["Cedula", "Placa", "Tipo", "Color", "Modelo"]
        anteriores_valores = [self._cliente.getCedula(), placa, tipo, color, modelo]

        if tipo == "Carro":
            self.field_frame = FieldFrame(
                self,
                "Criterio",
                [*anteriores_criterios, "Marca", "Tipo de carro", "Número de puestos"],
                "Valores",
                [*anteriores_valores, None, None, None],
                anteriores_criterios,
                combobox={
                    "Tipo de carro": ["Mecanico", "Automatico"],
                    "Marca": [m.name.title() for m in MarcasCarro],
                },
                titulo="Registro de carro",
            )
            self.field_frame.pack()
        else:
            self.field_frame = FieldFrame(
                self,
                "Criterio",
                [*anteriores_criterios, "Marca", "Tipo de moto", "Cilindraje"],
                "Valores",
                [*anteriores_valores, None, None, None],
                anteriores_criterios,
                combobox={
                    "Tipo de moto": ["Normal", "Alto cilindraje"],
                    "Marca": [m.name.title() for m in MarcasMoto],
                },
                titulo="Registro de moto",
            )
            self.field_frame.pack()

        self.btn_principal.config(command=self._terminar_registro)

    def _terminar_registro(self):
        placa = self.field_frame.getValue("Placa")
        tipo = self.field_frame.getValue("Tipo")
        color = self.field_frame.getValue("Color")
        modelo = self.field_frame.getValue("Modelo")
        marca = self.field_frame.getValue("Marca")

        if tipo == "Carro":
            puestos = int(self.field_frame.getValue("Número de puestos"))
            tipo_carro_str = self.field_frame.getValue("Tipo de carro")
            if tipo_carro_str == "Mecanico":
                tipo_carro = TipoVehiculo.MECANICO
            else:
                tipo_carro = TipoVehiculo.AUTOMATICO
            discapacitado = self._cliente.isDiscapacitado()
            vehiculo = Carro(
                placa,
                self._cliente,
                marca,
                color,
                modelo,
                tipo_carro,
                puestos,
                discapacitado,
            )
        else:
            cilindraje = int(self.field_frame.getValue("Cilindraje"))
            tipo_moto_str = self.field_frame.getValue("Tipo de moto")
            if tipo_moto_str == "Normal":
                tipo_moto = TipoVehiculo.NORMAL
            else:
                tipo_moto = TipoVehiculo.ALTOCC
            vehiculo = Moto(
                placa, self._cliente, marca, color, modelo, tipo_moto, cilindraje
            )

        self._baseDatos.registrarVehiculo(vehiculo)

        self.destroy()
        self._f_final(vehiculo)
