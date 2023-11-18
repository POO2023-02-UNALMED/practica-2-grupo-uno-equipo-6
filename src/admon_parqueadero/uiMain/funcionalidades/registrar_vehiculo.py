import tkinter as tk
from tkinter import messagebox
from typing import Any
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.gestorAplicacion.vehiculos.carro import Carro
from admon_parqueadero.gestorAplicacion.vehiculos.marcasCarro import MarcasCarro
from admon_parqueadero.gestorAplicacion.vehiculos.marcasMoto import MarcasMoto
from admon_parqueadero.gestorAplicacion.vehiculos.moto import Moto
from admon_parqueadero.gestorAplicacion.vehiculos.tipo_vehiculo import TipoVehiculo
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame
from admon_parqueadero.uiMain.componentes.formulario_cliente import FormularioCliente
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad


class RegistrarVehiculo(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.setTitulo("Registrar Vehiculo")
        self.setDescripcion("Bienvenido, aqui podra registrar un vehiculo, para empezar ingrese el número de cédula del dueño del vehiculo")

        #aca solo deberia acceder el administrador?

        self._inicio()

    def _inicio(self) -> None:
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        formulario = FormularioCliente(self.contenido, self.getBaseDatos(), f_final=self._inicio_registro)
        formulario.btn_principal.config(text="Continuar")
        formulario.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)

    def _inicio_registro(self, cliente: Cliente) -> None:
        tipos_vehiculo = ["Carro"]
        if not cliente.isDiscapacitado():
            tipos_vehiculo.append("Moto")

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

        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Cédula", "Placa", "Tipo", "Color", "Modelo"],
            "Valores",
            [str(cliente.getCedula()), None, None, None, None],
            ["Cédula"],
            combobox={"Tipo": tipos_vehiculo, "Color": coloresVehiculo},
            titulo="Registro de vehiculo",
        )

        self.field_frame.pack()

        self.botones = tk.Frame(self.contenido)
        self.botones.pack(side="bottom", fill="both", expand=True)
        self.btn_principal = tk.Button(
            self.botones, text="Continuar", command=lambda: self._continuar_registro(cliente)
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def _continuar_registro(self, cliente: Cliente) -> None:
        placa = self.field_frame.getValue("Placa") # errores ¿?
        tipo = self.field_frame.getValue("Tipo")
        color = self.field_frame.getValue("Color")
        modelo = self.field_frame.getValue("Modelo")
        
        vehiculo = self._baseDatos.buscarVehiculoRegistrado(placa)
        if vehiculo is not None:
            messagebox.showwarning("El vehiculo ya esta registrado", "El vehiculo ya se encuentra registrado")
            #raise ErrorUsuario(f"Vehiculo con placa {placa} ya registrado") no se deberian mostrar los errores con messagebox?
            return self._inicio_registro(cliente)
        
        self.field_frame.destroy()

        anteriores_criterios = ["Cedula", "Placa", "Tipo", "Color", "Modelo"]
        anteriores_valores = [cliente.getCedula(), placa, tipo, color, modelo]

        if tipo == "Carro":
            self.field_frame = FieldFrame(
                self.contenido,
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
                self.contenido,
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

        self.btn_principal.config(text="Aceptar", command=lambda: self._registrar(cliente))

    def _registrar(self, cliente: Cliente) -> None:
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
            discapacitado = cliente.isDiscapacitado()
            vehiculo = Carro(
                placa,
                cliente,
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
                placa, cliente, marca, color, modelo, tipo_moto, cilindraje
            )

        self._baseDatos.registrarVehiculo(vehiculo)
        cliente.agregarVehiculo(vehiculo)
        messagebox.showinfo("Registro exitoso", "El vehiculo ha sido registrado exitosamente")
        self.contenido.destroy()
        return self._inicio()
