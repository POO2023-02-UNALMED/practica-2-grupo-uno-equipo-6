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

    def filtrar (self):
        #! TODO : falta calcular los datos None en caso de no querer llenar un campo pueda obtener igual la lista de datos  Undefined 
        self.listaCarros = []
        
        if self.DiscapacidadA == 'Si':
            lista_aux = [vehiculo for vehiculo in self.all_vehiculo if vehiculo.isDiscapacitado() is True ]    
        elif self.DiscapacidadA == 'No':
            lista_aux = [vehiculo for vehiculo in self.all_vehiculo if vehiculo.isDiscapacitado() is False ]
        else :
            lista_aux = [] 
        
        for vehiculo in lista_aux:
            color = vehiculo.getColor()
            marca = vehiculo.getMarca()
            valorVehiculo = vehiculo.getPrecioVenta()
            
            self.colorSelected = self.field_frame.getValue('Color')
            self.MarcaSelected = self.field_frame.getValue('Marca')
            self.precioMaximoInput = self.field_frame.getValueNumero('Precio maximo',int)
            
            if (valorVehiculo < self.precioMaximoInput 
                and color == self.colorSelected 
                    and marca == self.MarcaSelected) :
                option=vehiculo.getPlaca() 
                self.listaCarros.append(option)
        self.listaCarros.append('No se encontraron registros') if len(self.listaCarros) == 0 else self.listaCarros



    def _configurar_ui(self, cliente: Cliente) -> None:
        self.nombreCliente = cliente.getNombre()
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
        
        self.EscogerVendedor()
    def EscogerVendedor (self):
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
            "Valores",
            None,
            None,
            {"Vendedor": self._vendedores_nombre},
            mensajeBienvenida
        )
        self.field_frame.pack()
        
        
        
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        
        self.btn_principal = tk.Button(
            self.frame_botones, text="Continuar", command=lambda: self.EscogerVehiculo()
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=self.field_frame.borrar
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)
        
        try:
            self.vendedorSelected = self.field_frame.getValue('Vendedor')
        except Exception as e :
            self.vendedorSelected = 'Undefined' 
    def EscogerVehiculo (self):

        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        mensajeVendedor = f"""Hola, te habla {self.vendedorSelected}
        """
        self.field_frame = FieldFrame(
        self.contenido,
        "Criterios",
        [ "Color","Marca", "Precio maximo","Adecuado Discapacidad"],
        "Valores",
        [None, None, None,None],
        None,
        combobox={
            "Color": list(self._vehiculos_color),
            "Marca":list(self._vehiculos_marca),
            "Adecuado Discapacidad": ['Si','No']
            }
        ,titulo=mensajeVendedor
        )
        self.field_frame.pack()
        
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        
        self.btn_principal = tk.Button(
            self.frame_botones, text="Continuar", command=lambda: self.ListaVehiculo()
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=self.field_frame.borrar
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)
        
        
        try : self.colorSelected = self.field_frame.getValue('Color') 
        except Exception as e : self.colorSelected = 'Undefined'
        try : self.precioMaximoInput = self.field_frame.getValue('Marca') 
        except Exception as e : self.precioMaximoInput = 'Undefined'
        try : self.MarcaSelected = self.field_frame.getValue('Precio maximo') 
        except Exception as e : self.MarcaSelected = 'Undefined'
        try : self.DiscapacidadA = self.field_frame.getValue('Adecuado Discapacidad') 
        except Exception as e : self.DiscapacidadA = 'Undefined'
        
    def ListaVehiculo (self):
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        self.filtrar()
        self.field_frame = FieldFrame(
            self.contenido,
            "",
            ["lista"],
            "",
            valores=[None],
            habilitado=None,
            combobox={"lista": self.listaCarros},
            titulo='Lista de carros disponibles'
        )
        self.field_frame.pack()
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        self.btn_principal = tk.Button(
            self.frame_botones, text="Seleccionar Vehiculo", command=lambda: self.facturacion()
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)
        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=self.field_frame.borrar
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

        self.VehiculoSelected = self.field_frame.getValue('lista')
    
    def facturacion (self):
        
        
        for vehicule in self.all_vehiculo:
            if self.VehiculoSelected == vehicule.getPlaca():
                vehiculo = vehicule
        try :
            self.vendedorSelected
            informacionVehiculo = [
                
            str(vehiculo.getMarca()),
            str(vehiculo.getModelo()),
            str(vehiculo.getPlaca()),
            str(vehiculo.getColor()),
            str(vehiculo.getPrecioVenta())]
            
            
            # TODO: generar id de factura 
            self.informacion_vehiculo.destroy()
            self.informacion_vehiculo = FieldFrame(
                self.contenido,
                "Campo",
                ["Vendedor","Marca","Modelo","placa","Color","precio"],
                "Informacion",
                valores=informacionVehiculo,
                habilitado=["Vendedor","Marca","Modelo","placa","Color","precio"],
                titulo='Informacion de modelo'
            )
            self.informacion_vehiculo.pack()
        except Exception as e :
            pass    