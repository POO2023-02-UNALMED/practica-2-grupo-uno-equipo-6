import tkinter as tk
 
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
        self.setDescripcion("""Bienvenido, aquí podrá comprar un carro según sus preferencias.
        Para comenzar, ingrese su documento, en caso de no estar registrado,
        ingrese sus datos""")
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        formulario = FormularioCliente(
            self.contenido, self.getBaseDatos(), f_final=self._configurar_ui
        )
        formulario.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)    


        
        # self.all_vehiculo = []
        # self.all_empleados = []
        # for parqueadero in parqueaderos:
        #     empleados = parqueadero.getEmpleados()
        #     vehiculosVentaParqueadero = parqueadero.getVehiculosVenta()
        #     self.all_vehiculo.extend(vehiculosVentaParqueadero)
        #     self.all_empleados.extend(empleados)
    
    def filtrar (self):
        self.listaCarros = []
        seleccion = self.seleccion.get()
        if seleccion == 1:
            lista_aux = [vehiculo for vehiculo in self.all_vehiculo if vehiculo.isDiscapacitado() is True ]    
        elif seleccion == 2:
            lista_aux = [vehiculo for vehiculo in self.all_vehiculo if vehiculo.isDiscapacitado() is False ]
        else :
            lista_aux = [] 
        for vehiculo in lista_aux:
            color = vehiculo.getColor()
            marca = vehiculo.getMarca()
            valorVehiculo = vehiculo.getPrecioVenta()
            
            self.colorSelected = self.getValue('Color')
            self.MarcaSelected = self.getValue('Marca')
            self.precioMaximoInput = self.getValueNumero('Precio maximo')
            if (valorVehiculo < self.precioMaximoInput 
                and color == self.colorSelected 
                    and marca == self.MarcaSelected) :
                option=vehiculo.getPlaca() 
                self.listaCarros.append(option)
        self.listaCarros.append('No se encontraron registros') if len(self.listaCarros) == 0 else self.listaCarros
       
                            

            
        
    def feedback():
        pass
        # 
    def _configurar_ui(self, cliente: Cliente) -> None:
       
        # mensaje de bienvenida
        nombre = cliente.getNombre()
        mensajeBienvenida = f"""Bienvenido de nuevo, {nombre}"""
        
        self._vendedores_nombre = list(
            map(lambda x: x.getNombre().title(), self._parqueadero.getVendedores())
        )

        self.all_vehiculo = [vehiculo for vehiculo in self._parqueadero.getVehiculosVenta() ]
        
        self._vehiculos_color = list(
            map(lambda x: x.getColor().title(), self.all_vehiculo)
        )
        
        self._vehiculos_marca = list(
            map(lambda x: x.getMarca().title(), self.all_vehiculo)
        )
        
        
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterios",
            ["Vendedor", "Color","Marca", "Precio maximo"],
            "Valores",
            [None,None, None, None],
            [None, None, None, None],
            combobox={"Vendedor": list(self._vendedores_nombre),
                      
                    "Color": list(self._vehiculos_color),
                    "Marca":list(self._vehiculos_marca)
                    }
            ,titulo=mensajeBienvenida
        )
        self.field_frame.pack()
        
       
        
        etiqueta_personalizada = tk.Label(self.contenido, text="Desea un vehiculo adaptado para condicion de discapacidad")
        etiqueta_personalizada.pack()
        self.seleccion = tk.IntVar()  # Variable para almacenar la opción seleccionada

        radio_btn1 = tk.Radiobutton(self.contenido, text="Si", variable=self.seleccion, value=1)
        radio_btn1.pack()

        radio_btn2 = tk.Radiobutton(self.contenido, text="No", variable=self.seleccion, value=2)
        radio_btn2.pack()
        
        # self.precioMaximoInput=entrada.get()
        # --discapacidad
        # Boton Consultar 
        
    
        BotonConsultar = tk.Button(self.contenido, text='Consultar',command=self.filtrar())
        BotonConsultar.pack()
        
        
        self.field_frame = FieldFrame(
            self.contenido,
            "",
            ["lista"],
            "",
            valores=[None],
            habilitado=[None],
            combobox={"lista": self.listaCarros},
            titulo='Lista de carros disponibles'
        )
        self.field_frame.pack()

        




