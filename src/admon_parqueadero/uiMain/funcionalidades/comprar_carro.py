import tkinter as tk
import tkinter as ttk
from typing import Any
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
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
        self.setDescripcion("Bienvenido, aquí podrá comprar un carro según sus preferencias.\
 Para comenzar, ingrese su documento, en caso de no estar registrado, \
 ingrese sus datos.")
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        formulario = FormularioCliente(
            self.contenido, self.getBaseDatos(), f_final=self._configurar_ui
        )
        formulario.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)
        

        
    def _configurar_ui(self, cliente: Cliente) -> None:
        
        # nombre = cliente.getNombre()
        # f"""Bienvenido de nuevo, {nombre}"""
        #! obtener una lista completa de todos los empleados de tipo Vendedor
        # Empleado.getCargo()=='Vendedor'
        
        # placas_vehiculos = map(lambda v: v.getPlaca(),cliente.getVehiculos() )
        placas_vehiculos=['ejemplo1']
        
        
        # r marca, color, precio máximo y en caso de que el cliente sea discapacitado entonces se le
        # dará una lista de carros que estarán previamente adaptados para especialmente personas discapacitadas.
        lista_vendedores=['prueba1']
        # selected_option = tk.StringVar()
        # filtro_vehiculos = ttk.Combobox(window, values=options, textvariable=selected_option)
        
        # v = getVehiculos()
        # v[0].getColor()
        # v[0].getMarca()
        # def precio_maximo (precioUsuario):
        #     v[0].get
        
        # combobox = ttk.Combobox(self.contenido, values=lista_vendedores)
        # combobox.pack()
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Vendedores", "Vehículo que desea comprar"],
            "Valor",
            [str(cliente.getCedula()), None],
            ["Cédula"],
            combobox={
                "Vehículo que desea comprar": [*placas_vehiculos]
            },
        )
        self.field_frame.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)
        # self._generar_botones("Continuar")#, lambda: self._continuar_inicio(cliente))
