import tkinter as tk
from tkinter import messagebox
from typing import Any, Optional, cast
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_producto import TipoProducto
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.gestorAplicacion.personas.empleado import Empleado
from admon_parqueadero.gestorAplicacion.vehiculos.carro import Carro
from admon_parqueadero.gestorAplicacion.vehiculos.moto import Moto
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame
from admon_parqueadero.uiMain.componentes.formulario_cliente import FormularioCliente
from admon_parqueadero.uiMain.componentes.formulario_vehiculo import FormularioVehiculo
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad


class Taller(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.setTitulo("Taller")

        self.setDescripcion(
            "Bienvenido al taller, será atendido por el mecánico de su preferencia.\
 Para hacer uso de los servicios del taller, su vehículo debe encontrarse en el\
 parqueadero. Para comenzar, ingrese sus datos y los de su vehículo."
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
            f_final=self._configurar_ingreso_taller,
        )
        formulario.pack()

    def _configurar_ingreso_taller(self, vehiculo: Vehiculo) -> None:
        if not vehiculo.estaParqueado():
            messagebox.showwarning(
                "El vehiculo no se encuentra en el parqueadero",
                "El vehiculo no se encuentra en el parqueadero, debe ingresarlo\
 en el apartado Ingresar vehiculo del menu procesos y consultas",
            )
            return self._configurar_ui(vehiculo.getDueno())

        self.contenido.destroy()
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        self._nombre_mecanicos = list(
            map(lambda x: x.getNombre().title(), self._parqueadero.getMecanicos())
        )

        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Mecanico"],
            "Valores",
            None,
            None,
            {"Mecanico": self._nombre_mecanicos},
            "Seleccione el mecanico de su preferencia",
        )
        self.field_frame.pack()

        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)

        self.btn_principal = tk.Button(
            self.frame_botones, text="Ingresar", command=lambda: self._taller(vehiculo)
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=self.field_frame.borrar
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def _taller(self, vehiculo: Vehiculo) -> None:
        eleccion_mecanico = self._nombre_mecanicos.index(
            self.field_frame.getValue("Mecanico")
        )
        mecanico = self._parqueadero.getMecanicos()[eleccion_mecanico]
        mensaje = f"Hola mi nombre es {mecanico.getNombre().title()} y voy a atenderlo.\
\n¿Que le vamos a hacer a su vehiculo hoy?"

        opciones = [
            "Revisión general",
            "Cambio de motor",
            "Cambio de transmision",
            "Cambio de acelerador",
            "Cambio de freno",
            "Cambio de bateria",
            "Cambio de deposito de gasolina",
            "Cambio de deposito de aceite",
            "Cambio de deposito de liquidos",
            "Cambio de llantas",
            "Cambio de rines",
        ]

        if isinstance(vehiculo, Carro):
            opciones.extend(["Cambio de pedal", "Cambio de amortiguadores"])
            posicion_producto = [
                "Delantera izq",
                "Delantera der",
                "Trasera izq",
                "Trasera der",
            ]
        else:
            opciones.extend(
                ["Cambio de cadena", "Cambio de pedales", "Cambio de amortiguador"]
            )
            posicion_producto = ["Delantera", "Trasera"]

        self.field_frame.destroy()
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Mecanico", "Escoja una opcion", "Escoja el producto a arreglar"],
            "Valores",
            [mecanico.getNombre().title(), None, None],
            ["Mecanico"],
            combobox={
                "Escoja una opcion": opciones,
                "Escoja el producto a arreglar": posicion_producto,
            },
            titulo=mensaje,
        )
        self.field_frame.cambiar_estado("Escoja el producto a arreglar", "disabled")
        self.field_frame.pack()

        self.frame_botones.destroy()
        self.frame_botones = tk.Frame(self.contenido)
        self.frame_botones.pack(side="bottom", fill="both", expand=True)

        def cambio_estado(event: tk.Event) -> None:
            opcion = event.widget.get()
            if opcion in [
                "Cambio de llantas",
                "Cambio de rines",
                "Cambio de amortiguadores",
            ]:
                self.field_frame.cambiar_estado(
                    "Escoja el producto a arreglar", "readonly"
                )  # TODO: implementar que se borre la seleccion en curso
            else:
                self.field_frame.cambiar_estado(
                    "Escoja el producto a arreglar", "disabled"
                )
            self.field_frame.pack()

        self.field_frame._entradas["Escoja una opcion"].bind(
            "<<ComboboxSelected>>", cambio_estado
        )  # preguntar como hacer esto sin acceder al atributo directamente

        self.btn_principal = tk.Button(
            self.frame_botones,
            text="Arreglar",
            command=lambda: self._arreglar(vehiculo, mecanico),
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.frame_botones, text="Borrar", command=self.field_frame.borrar
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

    def _arreglar(
        self, vehiculo: Vehiculo, mecanico: Empleado
    ) -> None:  # es mejor que esto retorne la funcion o la ejecute?
        opcion = self.field_frame.getValue("Escoja una opcion")
        if opcion == "Revisión general":
            self._revision_general(vehiculo, mecanico)
        else:
            nombre_producto = opcion.split(" ")[-1]
            self._cambio_de(nombre_producto, vehiculo, mecanico)

    def _revision_general(self, vehiculo: Vehiculo, mecanico: Empleado) -> None:
        componentes_dañados = mecanico.revisarVehiculo(vehiculo)

        if componentes_dañados:
            r = ""  # para guardar los componentes que se van a arreglar
            for producto in componentes_dañados:
                r += f"{producto.getTipo().__str__()}\n"
            nuevos_componentes = self._conseguir_repuestos(
                vehiculo, componentes_dañados
            )

            if nuevos_componentes is not None:
                messagebox.showinfo(
                    "Los siguientes componentes se arreglaran",
                    r,
                )
                for i in range(len(componentes_dañados)):
                    mecanico.cambiar(
                        componentes_dañados[i], nuevos_componentes[i], vehiculo
                    )
                    mecanico.setServiciosRealizados(
                        mecanico.getServiciosRealizados() + 1
                    )
            else:
                messagebox.showinfo(
                    "No podemos",
                    "No contamos con los recursos suficientes para realizar el servicio :(",
                )
                return self._taller(vehiculo)
        else:
            messagebox.showinfo("Que juicio", "Su vehiculo esta en perfecto estado")
            return self._taller(vehiculo)

    def _cambio_de(
        self, nombre_producto: str, vehiculo: Vehiculo, mecanico: Empleado
    ) -> None:
        almacen = self._parqueadero.getAlmacen()

        if nombre_producto == "llantas":
            # verificar para carro
            if isinstance(vehiculo, Carro):
                posiciones = [
                    "Delantera izq",
                    "Delantera der", 
                    "Trasera izq",
                    "Trasera der"
                ]
                llanta_elegida = posiciones.index(
                    self.field_frame.getValue("Escoja el producto a arreglar")
                )
                llanta_v = cast(Carro, vehiculo).getLlantas()[llanta_elegida]
                if almacen.existeProducto(TipoProducto.LLANTA):
                    llanta_n = almacen.conseguirProducto(TipoProducto.LLANTA)
                    if llanta_n is not None:
                        vehiculo.getDueno().getFactura().agregarProducto(
                            llanta_n, 1
                        )  # por ahora se agrega el numero de veces del servicio o producto
                        vehiculo.getDueno().getFactura().agregarServicio(
                            "Cambio de llantas", 1
                        )  # sera mejor agregar el valor ¿?
                        mecanico.cambiar(llanta_v, llanta_n, vehiculo)
                        mecanico.setServiciosRealizados(
                            mecanico.getServiciosRealizados() + 1
                        )
                        messagebox.showinfo(
                            "*Sonidos de mecanico*", "Listo, como nuevo :)"
                        )
                else:
                    messagebox.showwarning(
                        "No podemos",
                        "No contamos con los recursos suficientes para realizar el servicio :(",
                    )
                    return self._taller(vehiculo)
            else:
                # para moto
                posiciones = ["Delantera", "Trasera"]
                llanta_elegida = posiciones.index(
                    self.field_frame.getValue("Escoja el producto a arreglar")
                )
                llanta_v = cast(Moto, vehiculo).getLlantas()[llanta_elegida]
                if almacen.existeProducto(TipoProducto.LLANTA):
                    llanta_n = almacen.conseguirProducto(TipoProducto.LLANTA)
                    if llanta_n is not None:
                        vehiculo.getDueno().getFactura().agregarProducto(llanta_n, 1)
                        vehiculo.getDueno().getFactura().agregarServicio(
                            "Cambio de llantas", 1
                        )
                        mecanico.cambiar(llanta_v, llanta_n, vehiculo)
                        mecanico.setServiciosRealizados(
                            mecanico.getServiciosRealizados() + 1
                        )
                        messagebox.showinfo(
                            "*Sonidos de mecanico*", "Listo, como nuevo :)"
                        )
                else:
                    messagebox.showwarning(
                        "No podemos",
                        "No contamos con los recursos suficientes para realizar el servicio :(",
                    )
                    return self._taller(vehiculo)
                
        if nombre_producto == "rines":
            # verificar para carro
            if isinstance(vehiculo, Carro):
                posiciones = [
                    "Delantera izq",
                    "Delantera der",
                    "Trasera izq",
                    "Trasera der"
                ]
                rin_elegido = posiciones.index(
                    self.field_frame.getValue("Escoja el producto a arreglar")
                )
                rin_v = cast(Carro, vehiculo).getLlantas()[rin_elegido]
                if almacen.existeProducto(TipoProducto.RIN):
                    rin_n = almacen.conseguirProducto(TipoProducto.RIN)
                    if rin_n is not None:
                        vehiculo.getDueno().getFactura().agregarProducto(
                            rin_n, 1
                        )  # por ahora se agrega el numero de veces del servicio o producto
                        vehiculo.getDueno().getFactura().agregarServicio(
                            "Cambio de rines", 1
                        )  # sera mejor agregar el valor ¿?
                        mecanico.cambiar(rin_v, rin_n, vehiculo)
                        mecanico.setServiciosRealizados(
                            mecanico.getServiciosRealizados() + 1
                        )
                        messagebox.showinfo(
                            "*Sonidos de mecanico*", "Listo, como nuevo :)"
                        )
                else:
                    messagebox.showwarning(
                        "No podemos",
                        "No contamos con los recursos suficientes para realizar el servicio :(",
                    )
                    return self._taller(vehiculo)
            else:
                # para moto
                posiciones = ["Delantera", "Trasera"]
                rin_elegido = posiciones.index(
                    self.field_frame.getValue("Escoja el producto a arreglar")
                )
                rin_v = cast(Moto, vehiculo).getLlantas()[rin_elegido]
                if almacen.existeProducto(TipoProducto.RIN):
                    rin_n = almacen.conseguirProducto(TipoProducto.RIN)
                    if rin_n is not None:
                        vehiculo.getDueno().getFactura().agregarProducto(rin_n, 1)
                        vehiculo.getDueno().getFactura().agregarServicio(
                            "Cambio de rines", 1
                        )
                        mecanico.cambiar(rin_v, rin_n, vehiculo)
                        mecanico.setServiciosRealizados(
                            mecanico.getServiciosRealizados() + 1
                        )
                        messagebox.showinfo(
                            "*Sonidos de mecanico*", "Listo, como nuevo :)"
                        )
                else:
                    messagebox.showwarning(
                        "No podemos",
                        "No contamos con los recursos suficientes para realizar el servicio :(",
                    )
                    return self._taller(vehiculo)

        if nombre_producto == "amortiguadores":
            posiciones = ["Delantera izq", "Delantera der", "Trasera izq", "Trasera der"]
            amortiguador_elegido = posiciones.index(
                self.field_frame.getValue("Escoja el producto a arreglar")
            )
            amortiguador_v = cast(Carro, vehiculo).getAmortiguadores()[
                amortiguador_elegido
            ]
            if almacen.existeProducto(TipoProducto.AMORTIGUADOR):
                amortiguador_n = almacen.conseguirProducto(TipoProducto.AMORTIGUADOR)
                if amortiguador_n is not None:
                    vehiculo.getDueno().getFactura().agregarProducto(amortiguador_n, 1)
                    vehiculo.getDueno().getFactura().agregarServicio(
                        "Cambio de amortiguadores", 1
                    )
                    mecanico.cambiar(amortiguador_v, amortiguador_n, vehiculo)
                    mecanico.setServiciosRealizados(
                        mecanico.getServiciosRealizados() + 1
                    )
                    messagebox.showinfo("*Sonidos de mecanico*", "Listo, como nuevo :)")
            else:
                messagebox.showwarning(
                    "No podemos",
                    "No contamos con los recursos suficientes para realizar el servicio :(",
                )
                return self._taller(vehiculo)

        # para el resto de productos
        tipo_producto = TipoProducto[nombre_producto.upper()]
        if almacen.existeProducto(tipo_producto):
            productos = [tipo for tipo in TipoProducto.__members__.values()]
            producto_v = self._conseguir(productos.index(tipo_producto), vehiculo)
            producto_n = almacen.conseguirProducto(tipo_producto)
            if producto_n is not None and producto_v is not None:
                vehiculo.getDueno().getFactura().agregarProducto(producto_n, 1)
                vehiculo.getDueno().getFactura().agregarServicio(
                    f"Cambio de {tipo_producto.name.title()}s", 1
                )
                mecanico.cambiar(producto_v, producto_n, vehiculo)
                mecanico.setServiciosRealizados(mecanico.getServiciosRealizados() + 1)
                messagebox.showinfo("*Sonido de mecanico*", "Listo como nuevo :)")
        else:
            messagebox.showwarning(
                "No podemos",
                "No contamos con los recursos suficientes para realizar el servicio :(",
            )
            return self._taller(vehiculo)

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

    # metodo para conseguir el componente de un vehiculo (hacerlo mejor jajajajja)
    def _conseguir(self, i: int, vehiculo: Vehiculo) -> Optional[Producto]:
        r: Optional[Producto] = None
        if isinstance(vehiculo, Carro):
            if i == 0:
                r = vehiculo.getMotor()
            elif i == 1:
                r = vehiculo.getTransmision()
            elif i == 2:
                r = vehiculo.getAcelerador()
            elif i == 3:
                r = vehiculo.getFreno()
            elif i == 4:
                r = vehiculo.getBateria()
            elif i == 5:
                r = vehiculo.getDepositos()[0]
            elif i == 6:
                r = vehiculo.getDepositos()[1]
            elif i == 7:
                r = vehiculo.getDepositos()[2]
            elif i == 10:
                r = vehiculo.getPedal()

        elif isinstance(vehiculo, Moto):
            if i == 0:
                r = vehiculo.getMotor()
            elif i == 1:
                r = vehiculo.getTransmision()
            elif i == 2:
                r = vehiculo.getAcelerador()
            elif i == 3:
                r = vehiculo.getFreno()
            elif i == 4:
                r = vehiculo.getBateria()
            elif i == 5:
                r = vehiculo.getDepositos()[0]
            elif i == 6:
                r = vehiculo.getDepositos()[1]
            elif i == 7:
                r = vehiculo.getDepositos()[2]
            elif i == 11:
                r = vehiculo.getCadena()
            elif i == 12:
                r = vehiculo.getPedales()
            elif i == 13:
                r = vehiculo.getAmortiguador()

        return r
