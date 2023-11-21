# Funcionalidad del módulo: Contiene la clase VenderCarro, que hereda de BaseFuncionalidad,
#permite que el cliente le venda un vehiculo al parqueadero, sea por dinero o cambiar por otro
#carro que se encuentre disponible para la venta.
#Componentes del módulo: VenderCarro
#Autores: Sara

import tkinter as tk
from tkinter import messagebox
from typing import Any, Optional, cast
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad
from admon_parqueadero.uiMain.componentes.formulario_cliente import FormularioCliente
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame
from admon_parqueadero.uiMain.componentes.formulario_carro import FormularioCarro
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo
from admon_parqueadero.gestorAplicacion.parqueadero.plaza import Plaza
from admon_parqueadero.gestorAplicacion.vehiculos.marcasCarro import MarcasCarro
from admon_parqueadero.gestorAplicacion.parqueadero.almacen import Almacen
from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto
from admon_parqueadero.gestorAplicacion.vehiculos.carro import Carro



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
            self.contenido, self.getBaseDatos(), f_final=self._configurar_ui, imprimir=self.imprimir
        )
        formulario.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)

    def _configurar_ui(self, cliente: Cliente) -> None:
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        self._cliente = cliente
        formulario = FormularioCarro(
            self.contenido,
            self.getBaseDatos(),
            cliente,
            f_final=self._configurar_ingreso_venta,
        )
        formulario.pack()
    def _configurar_ingreso_venta(self, vehiculo: Vehiculo):
        self._vehiculo = vehiculo
        if vehiculo.estaParqueado():
            return self.escoger_vendedor(vehiculo)

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
            titulo="Seleccione la plaza",
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
        self._vehiculo = cast(Vehiculo, self.getBaseDatos().buscarVehiculoRegistrado(placa))
        plaza = cast(Plaza, self.getParqueadero().buscarPlaza(plaza_num))
        self.getParqueadero().ingresarVehiculo(self._vehiculo, plaza)

        # TODO: Generar factura

        self.imprimir("Vehículo ingresado")
        self._configurar_ui(self._vehiculo.getDueno())
    
    #Mostrar lista de vendedores disponibles
    def escoger_vendedor(self, vehiculo: Vehiculo):
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        self._vendedor = None
        self._vendedores_nombre = list(
            map(lambda x: x.getNombre().title(), self._parqueadero.getVendedores())
        )
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Vendedor"],
            "Valores",
            None,
            None,
            {"Vendedor": self._vendedores_nombre},
            "Seleccione al vendedor de su preferencia",
        )
        self.field_frame.pack()

        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        self.btn_principal = tk.Button(
            self.frame_botones, text="Continuar", command=lambda: self.continuarVenta(vehiculo)
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def precioMaximo(self, vehiculo: Vehiculo):
        marca_carro_venta = vehiculo.getMarca()
        if marca_carro_venta == MarcasCarro.TOYOTA.name.title():
            self._precio_maximo = MarcasCarro.TOYOTA.value
        elif marca_carro_venta == MarcasCarro.RENAULT.name.title():
            self._precio_maximo = MarcasCarro.RENAULT.value
        elif marca_carro_venta == MarcasCarro.MAZDA.name.title():
            self._precio_maximo = MarcasCarro.MAZDA.value
        elif marca_carro_venta == MarcasCarro.KIA.name.title():
            self._precio_maximo = MarcasCarro.KIA.value
        elif marca_carro_venta == MarcasCarro.CHEVROLET.name.title():
            self._precio_maximo = MarcasCarro.CHEVROLET.value
        #else:
        #self._precio_maximo = 50000000
        return self._precio_maximo
    

    def continuarVenta(self, vehiculo: Vehiculo) -> None:
        if self._vendedor==None:
    
            eleccion_vendedor = self._vendedores_nombre.index(
                self.field_frame.getValue("Vendedor")
            )
            self._vendedor = self._parqueadero.getVendedores()[eleccion_vendedor]
            self.imprimir(f"Hola, mi nombre es {self._vendedor.getNombre().title()} y voy a atenderlo el día de hoy.")

        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Precio"],
            "Valores",
            None,
            None,
            titulo="Ingrese el precio por el que desea vender su carro al parqueadero",
        )
        self.field_frame.pack()
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        self.btn_principal = tk.Button(
            self.frame_botones, text="Continuar", command=lambda: self.escogerMecanico(vehiculo)
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def escogerMecanico(self, vehiculo: Vehiculo):
        self._precio_cliente = self.field_frame.getValueNumero("Precio", int)
        self._precio_maximo = self.precioMaximo(vehiculo)
        if self._precio_cliente>self._precio_maximo:
            messagebox.showinfo(
                    "No podemos",
                    "El precio ingresado no es aceptado por el parqueadero, intente realizar otra oferta.",
                )
            return self.continuarVenta(vehiculo)
        self.imprimir("Su carro será revisado en el taller, y se le dará una oferta de compra.")

        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        self._mecanicos_nombre = list(
            map(lambda x: x.getNombre().title(), self._parqueadero.getMecanicos())
        )
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Mecanico"],
            "Valores",
            None,
            None,
            {"Mecanico": self._mecanicos_nombre},
            "Seleccione al mecánico de su preferencia",
        )
        self.field_frame.pack()


        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        self.btn_principal = tk.Button(
            self.frame_botones, text="Continuar", command=lambda: self.revisionTaller(vehiculo)
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def revisionTaller(self, vehiculo:Vehiculo):

        eleccion_mecanico = self._mecanicos_nombre.index(
            self.field_frame.getValue("Mecanico")
        )
        self._mecanico = self._parqueadero.getMecanicos()[eleccion_mecanico]

        #Cotizacion del parqueadero, le resta los productos malos al valor máximo que se paga por el carro
        self._productosMalos = self._mecanico.revisarVehiculo(vehiculo)
        if self._productosMalos:
            for i in range(len(self._productosMalos)-1): #Genera error unhashable type: Producto
                self._precio_maximo -= self._parqueadero.getAlmacen().cotizarProducto(self._productosMalos[i].getTipo())
        
        self._mecanico.setServiciosRealizados(self._mecanico.getServiciosRealizados()+1)
        #self._cliente.getFactura().agregarServicio("Revision general", 1)

        if self._precio_cliente<=self._precio_maximo:
            self._precio_final=self._precio_cliente
        else:
            self._precio_final=self._precio_maximo
    
        self.imprimir(f"Hola, mi nombre es {self._mecanico.getNombre().title()} y voy a atenderlo el día de hoy.")
        
        #return self.terminar_venta(vehiculo)
        self.imprimir(f"El parqueadero ha realizado la revisión del vehículo, y le presenta la siguiente oferta:\nPuede vender su vehículo por {self._precio_final} o puede cambiar su vehículo por uno disponible en el rango de precio.")
        opciones = [
            f"Aceptar la oferta de {self._precio_final}",
            "Cambiar por otro carro"
        ]
        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Seleccione una opción"],
            "Valores",
            None,
            None,
        combobox={
            "Seleccione una opción": opciones,
        },
        titulo="Seleccione la oferta que desea aceptar.",
        )
        self.field_frame.pack()
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)
        self.btn_principal = tk.Button(
            self.frame_botones, text="Continuar", command=lambda: self.finalizar_compra(vehiculo)
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)


    def finalizar_compra(self, vehiculo:Vehiculo):
        eleccion = self.field_frame.getValue("Seleccione una opción")

        if eleccion=="Cambiar por otro carro":
            self.contenido.destroy()
            self.contenido = tk.Frame(self.frame_contenido)
            self.packContenido(self.contenido)

            self.vehiculos_rango_precio = list(
                filter(lambda x: x.getPrecioVenta()<=self._precio_final, self._parqueadero.getVehiculosVenta())
            )
            info_carros_venta = list(
                map(lambda x: x.getPlaca(), self.vehiculos_rango_precio)
            )
            self.field_frame = FieldFrame(
                self.contenido,
                "Criterio",
                ["Seleccione el vehiculo de su preferencia"],
                "Valores",
                None,
                None,
                combobox={
                    "Seleccione el vehiculo de su preferencia": info_carros_venta,
                },
            )
            self.field_frame.pack()
            self.frame_botones = tk.Frame(self.contenido)
            self.frame_botones.pack(side="bottom", fill="both", expand=True)
            self.btn_principal = tk.Button(
                self.frame_botones, text="Continuar", command=lambda: self.cambiar_carro(vehiculo)
            )
            self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

            self.btn_borrar = tk.Button(
                self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
            )
            self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)
            
        else: #Vender por el precio
            self.contenido.destroy()
            self.contenido = tk.Frame(self.frame_contenido)
            self.packContenido(self.contenido)
            self.field_frame = FieldFrame(
                self.contenido,
                "Criterios",
                [],
                "Valores",
                None,
                None,
                {},
                titulo = "Se ha finalizado la venta."
            )
            self.field_frame.pack()
            productosNuevos = self._conseguir_repuestos(
                vehiculo, self._productosMalos
            )
            if productosNuevos:
                for i in range(len(self._productosMalos)):
                    self._mecanico.cambiar(
                        self._productosMalos[i], productosNuevos[i], vehiculo
                    )
                    self._mecanico.setServiciosRealizados(
                        self._mecanico.getServiciosRealizados() + 1
                    )
            self._vendedor.setServiciosRealizados(self._vendedor.getServiciosRealizados()+1)
            indiceVehiculo = self._cliente.getVehiculos().index(vehiculo)
            self._cliente.getVehiculos().pop(indiceVehiculo)
            vehiculo.setDueno(None)
            cast(Carro, vehiculo).setPrecioVenta(50000000)
            self._parqueadero.agregarVehiculoVenta(vehiculo)
            self.frame_botones = tk.Frame(self.contenido)
            self.frame_botones.pack(side="bottom", fill="both", expand=True)
            self.btn_principal = tk.Button(
                self.frame_botones, text="Continuar", command=lambda: mensaje_final()
            )
            self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

            self.btn_borrar = tk.Button(
                self.frame_botones, text="Borrar", command=lambda: self.field_frame.borrar()
            )
            self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)
            
            def mensaje_final():
                opcion = messagebox.showinfo("Venta finalizada", f"¡Felicidades! Se ha añadido el monto de {self._precio_final} a su cuenta. Ha finalizado la venta de carro, ¡vuelva pronto!")
                if opcion:
                    return self.finalizar()
            


    def cambiar_carro(self, vehiculo: Vehiculo):
        eleccionCarro = self.field_frame.getValue("Seleccione el vehiculo de su preferencia") #Me da la placa del carro 
        for carro in self.vehiculos_rango_precio:
            if carro.getPlaca()==eleccionCarro:
                carroNuevo = carro
                break
        
        infoCarro = [
            "Información sobre el carro escogido: ",
            f"Placa: {carroNuevo.getPlaca()}",
            f"Marca: {carroNuevo.getMarca()}",
            f"Modelo: {carroNuevo.getModelo()}",
            f"Color: {carroNuevo.getColor()}",
            f"Precio de venta: {str(carroNuevo.getPrecioVenta())}",
        ]
        
        for info in infoCarro:
            self.imprimir(info)
        carroNuevo.setDueno(self._cliente)
        indiceCarroNuevo = self._parqueadero.getVehiculosVenta().index(carroNuevo)
        self._parqueadero.getVehiculosVenta().pop(indiceCarroNuevo)
        excedente = self._precio_final - carroNuevo.getPrecioVenta()
        carroNuevo.setPrecioVenta(0)
        self._vendedor.setServiciosRealizados(self._vendedor.getServiciosRealizados()+1)
        #Arreglar los componentes malos 
        productosNuevos = self._conseguir_repuestos(
            vehiculo, self._productosMalos
        )

        for i in range(len(self._productosMalos)):
                    self._mecanico.cambiar(
                        self._productosMalos[i], productosNuevos[i], vehiculo
                    )
                    self._mecanico.setServiciosRealizados(
                        self._mecanico.getServiciosRealizados() + 1
                    )
        indiceVehiculo = self._cliente.getVehiculos().index(vehiculo)
        self._cliente.getVehiculos().pop(indiceVehiculo)
        vehiculo.setDueno(None)
        cast(Carro, vehiculo).setPrecioVenta(50000000)
        self._parqueadero.agregarVehiculoVenta(vehiculo)
        messagebox.showinfo("Cambio realizado", f"Hemos realizado el intercambio de carros, ¡Felicidades! El excedente de {excedente} se ha añadido a su cuenta. Ha finalizado la venta, ¡vuelva pronto!")
        
        return self.finalizar()



    def _conseguir_repuestos(
        self, vehiculo: Vehiculo, productos: list[Producto]
    ) -> Optional[list[Producto]]:
        almacen = self._parqueadero.getAlmacen()
        productos_vendidos: list[Producto] = []

        for p in productos:
            if almacen.existeProducto(p.getTipo()):
                n_producto = almacen.conseguirProducto(p.getTipo())
                if n_producto is not None:
                    n_producto.setMarca(vehiculo.getMarca())
                    n_producto.setPrecio(0)
                    productos_vendidos.append(n_producto)
                vehiculo.getDueno().getFactura().agregarProducto(p, 1)
            else:
                return None
        return productos_vendidos
    
    def finalizar(self):
        return self._configurar_ui(self._cliente)
