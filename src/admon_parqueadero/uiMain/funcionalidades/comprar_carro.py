import tkinter as tk
 
from typing import Any, cast
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.vehiculos.carro import Carro
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
        self.cliente = cliente
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
            self.frame_botones, text="Continuar", command=lambda: self.EscogerVehiculo()
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=self.field_frame.borrar
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)
         
    def EscogerVehiculo (self):
        if self.vendedorSelected == None:
            self.vendedorSelected = self.field_frame.getValue('Vendedor')
            self.imprimir(f"""Hola, te habla {self.vendedorSelected}
            """)
        
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        self.field_frame = FieldFrame(
        self.contenido,
        "Criterio",
        [ "Color","Marca", "Precio maximo","Adecuado Discapacidad"],
        "Valor",
        [None, None, None,None],
        None,
        combobox={
            "Color": list(self._vehiculos_color),
            "Marca":list(self._vehiculos_marca),
            "Adecuado Discapacidad": ['Si','No']
            }
        ,titulo="Seleccione las características que desea en su carro nuevo."
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
        self.imprimir("Seleccione el color y marca que desea, y si necesita que esté adecuado para discapacidad.")
        
        
    def ListaVehiculo (self):
        self.colorSelected = self.field_frame.getValue('Color') 
        self.precioMaximoInput = self.field_frame.getValueNumero('Precio maximo', float) 
        self.MarcaSelected = self.field_frame.getValue('Marca') 
        self.DiscapacidadA = self.field_frame.getValue('Adecuado Discapacidad') 
        self.filtrar()
        if self.listaCarros[0]=='No se encontraron registros':
            self.imprimir("No se encontraron carros con esas características")
            return self.EscogerVehiculo()
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        self.field_frame = FieldFrame(
            self.contenido,
<<<<<<< Updated upstream
            "",
            ["Carros disponibles"],
            "",
=======
            "Criterio",
            ["lista"],
            "Valor",
>>>>>>> Stashed changes
            valores=[None],
            habilitado=None,
            combobox={"Carros disponibles": self.listaCarros},
            titulo='Lista de carros disponibles con las carácteristicas seleccionadas'
        )
        self.field_frame.pack()
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        self.btn_principal = tk.Button(
            self.frame_botones, text="Seleccionar Vehiculo", command=lambda: self.seleccionar_carro()
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)
        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=self.field_frame.borrar
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)
        self.imprimir("Seleccione una placa de la lista de carros disponibles, y se le mostrarán las demás características del carro.")
    
    def seleccionar_carro(self):
        self.seleccion_carro = self.field_frame.getValue("lista")
        
        placas_carro_venta = map(lambda x: x.getPlaca().upper(), self._parqueadero.getVehiculosVenta())
        carroComprado = self._parqueadero.getVehiculosVenta()[[*placas_carro_venta].index(self.seleccion_carro)]
        
        if carroComprado is not None: #manejar error?
            infoCarro = [
                "Información sobre el carro escogido: ",
                f"Placa: {carroComprado.getPlaca()}",
                f"Marca: {carroComprado.getMarca()}",
                f"Modelo: {carroComprado.getModelo()}",
                f"Color: {carroComprado.getColor()}",
                f"Precio de venta: {str(carroComprado.getPrecioVenta())}",
            ]
        
            for info in infoCarro:
                self.imprimir(info) 
        
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
            self.frame_botones, text="Borrar", command=self.field_frame.borrar
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def finalizar_venta(self, carro: Carro):
        seleccion = self.field_frame.getValue("¿Desea comprar este carro?")
        if seleccion == "No":
            return self.EscogerVehiculo()

        carro.setDueno(self.cliente)
        carro.setPrecioVenta(0)
        self.cliente.getVehiculos().append(carro)
        indiceCarro = self._parqueadero.getVehiculosVenta().index(carro)
        self._parqueadero.getVehiculosVenta().pop(indiceCarro)
        self.imprimir("¡Felicidades! Ha comprado el carro, esperamos que lo disfrute. Vuelva pronto.")
        return self._configurar_ui(self.cliente)
