import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from typing import Any, Callable, Literal
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.parqueadero.producto import Producto
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_estado import TipoEstado
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_producto import TipoProducto
from admon_parqueadero.gestorAplicacion.personas.empleado import Empleado
from admon_parqueadero.gestorAplicacion.vehiculos.carro import Carro
from admon_parqueadero.gestorAplicacion.vehiculos.coloresVehiculo import ColoresVehiculo
from admon_parqueadero.gestorAplicacion.vehiculos.marcasCarro import MarcasCarro
from admon_parqueadero.gestorAplicacion.vehiculos.tipo_vehiculo import TipoVehiculo
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad


class ManejoParqueadero(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.setTitulo("Manejo Parqueadero")
        self.setDescripcion(
            "Bienvenido. Para acceder al manejo del parqueadero, debe ingresar la cédula del administrador. Aquí podrá contratar y despedir empleados, manejar productos, generar bonificaciones, entre otras funciones de la administración del parqueadero."
        )

        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)
        self.botones = tk.Frame(self.contenido)
        self.botones.pack(side="bottom", fill="both", expand=True)

        self.btn_principal = tk.Button(
            self.botones, text="Ingresar", command=self._principal
        )
        self.btn_principal.pack(side="left", fill="both", expand=True, padx=15)

        self.btn_borrar = tk.Button(
            self.botones, text="Borrar"
        )
        self.btn_borrar.pack(side="right", fill="both", expand=True, padx=15)

        self._inicio()

    def _inicio(self) -> None:
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Cédula"],
            "Valor",
            None,
            None,
            titulo="Ingrese la cédula del administrador",
        )
        self.field_frame.pack()

        self.btn_principal.config(text="Ingresar", command=self._principal)
        self.btn_borrar.config(command=lambda: self.field_frame.borrar())

    def _principal(self) -> None:
        cedula = self.field_frame.getValueNumero("Cédula", int)
        admin = self._parqueadero.getAdministrador()
        if admin is not None:
            if cedula != admin.getCedula():
                messagebox.showerror("Acceso denegado", "Cedula incorrecta")
                self.field_frame.destroy()
                return self._inicio()

            self._administrador = admin
            self.field_frame.destroy()
            self.field_frame = FieldFrame(
                self.contenido,
                "Criterio",
                ["Parte del parqueadero a manejar"],
                "Valor",
                None,
                None,
                {
                    "Parte del parqueadero a manejar": [
                        "Parqueadero",
                        "Taller",
                        "Almacen",
                    ]
                },
                titulo=f"Bienvenido {admin.getNombre()}\nSeleccione la parte del parqueadero a manejar",
            )
        else:
            messagebox.showerror("Error", "No hay administrador registrado en el sistema")
            return self._inicio()
        self.field_frame.pack()
        self.btn_principal.config(text="Continuar", command=self._ingreso)

    def _ingreso(self) -> None:
        opcion = self.field_frame.getValue("Parte del parqueadero a manejar")
        # opciones = {"Parqueadero": lambda: self._manejo_parqueadero, "Taller": lambda: self._manejo_taller, "Almacen": self._manejo_almacen}
        if opcion == "Parqueadero":
            return self._manejo_parqueadero()
        elif opcion == "Taller":
            return self._manejo_taller()
        else:
            return self._manejo_almacen()

    # metodo que recibe una funcion de tipo _manejo_... y ejecuta la opcion escogida para al final regresar a la funcion desde donde se llame el metodo
    def _manejo(self, funcion_manejo: Callable[[], None]) -> None:
        opcion = self.field_frame.getValue("Opciones")
        funcionalidades: dict[str, Callable] = {
            "Agregar carro para venta": self._agregar_carro_venta,
            "Agregar plazas": self._agregar_plazas,
            "Contratar vendedor": self._agregar_empleado,
            "Despedir vendedor": self._despedir_empleado,
            "Retirar vehículo": self._retirar_vehiculo,
            "Ver información de un cliente": self._informacion_cliente,
            "Contratar mecanico": self._agregar_empleado,
            "Despedir mecanico": self._despedir_empleado,
            "Ver estadisticas de los mecanicos": self._estadisticas_mecanicos,
            "Generar bonificaciones para los mecanicos": self._bonificaciones_mecanicos,
            "Agregar producto al almacen": self._agregar_producto_almacen,
            "Ver inventario del almacen": self._inventario_almacen,
        }
        if opcion in ["Contratar vendedor", "Despedir vendedor"]:
            return funcionalidades[opcion]("Vendedor", funcion_manejo)
        elif opcion in ["Contratar mecanico", "Despedir mecanico"]:
            return funcionalidades[opcion]("Mecanico", funcion_manejo)
        else:
            return funcionalidades[opcion](funcion_manejo)

    def _manejo_parqueadero(self) -> None:
        self.field_frame.destroy()
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Opciones"],
            "Valor",
            None,
            None,
            {
                "Opciones": [
                    "Agregar carro para venta",
                    "Agregar plazas",
                    "Contratar vendedor",
                    "Despedir vendedor",
                    "Retirar vehículo",
                    "Ver información de un cliente",
                ]
            },
            titulo="Parqueadero"
        )
        self.field_frame.pack()
        self.btn_principal.config(
            text="Continuar",
            command=lambda: self._manejo(self._manejo_parqueadero)
        )

    def _manejo_taller(self) -> None:
        self.field_frame.destroy()
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Opciones"],
            "Valor",
            None,
            None,
            {
                "Opciones": [
                    "Contratar mecanico",
                    "Despedir mecanico",
                    "Ver estadisticas de los mecanicos",
                    "Generar bonificaciones para los mecanicos",
                ]
            },
            titulo="Taller",
        )
        self.field_frame.pack()
        self.btn_principal.config(
            text="Continuar",
            command=lambda: self._manejo(self._manejo_taller)
        )

    def _manejo_almacen(self) -> None:
        self.field_frame.destroy()
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Opciones"],
            "Valor",
            None,
            None,
            {"Opciones": ["Agregar producto al almacen", "Ver inventario del almacen"]},
            titulo="Almacen",
        )
        self.field_frame.pack()
        self.btn_principal.config(
            text="Continuar",
            command=lambda: self._manejo(self._manejo_almacen)
        )

    # metodos de ayuda
    # metodos para agregar un carro a ventas o un nuevo vendedor o mecanico
    def _agregar_carro(self, funcion_manejo: Callable[[], None]) -> None:
        placa = self.field_frame.getValue("Placa")
        if placa in map(lambda v: v.getPlaca(), self._parqueadero.getVehiculosVenta()):
            messagebox.showerror(
                "El carro ya existe",
                "Un carro con estas caracteristicas ya se encuentra para venta",
            )
            return funcion_manejo()
        marca = self.field_frame.getValue("Marca")
        color = self.field_frame.getValue("Color")
        modelo = self.field_frame.getValue("Modelo")
        tipo_carro = TipoVehiculo.AUTOMATICO
        if self.field_frame.getValue("Tipo") == "Mecanico":
            tipo_carro = TipoVehiculo.MECANICO
        puestos = self.field_frame.getValueNumero("Puestos", int)
        precio_venta = self.field_frame.getValueNumero("Precio", float)

        carro_venta = Carro(
            placa,
            None,
            marca,
            color,
            modelo,
            tipo_carro,
            puestos,
            False,
            precio_venta,
        )
        self._parqueadero.agregarVehiculoVenta(carro_venta)
        messagebox.showinfo("Vehiculo agregado", "El carro se ha agregado exitosamente")
        return funcion_manejo()

    def _agregar(self, tipo: Literal["Mecanico", "Vendedor"], funcion_manejo: Callable[[], None]) -> None:
        cedula = self.field_frame.getValueNumero("Cédula", int)
        if self._parqueadero.existeEmpleado(cedula):
            messagebox.showerror(
                "El empleado ya existe", f"El empleado con cédula {cedula} ya existe"
            )
            return funcion_manejo()
        nombre = self.field_frame.getValue("Nombre")
        telefono = self.field_frame.getValueNumero("Teléfono", int)
        correo = self.field_frame.getValue("Correo")
        direccion = self.field_frame.getValue("Dirección")
        salario = self.field_frame.getValueNumero("Salario", float)
        empleado = Empleado(nombre, cedula, telefono, correo, direccion, tipo, salario)
        self._parqueadero.agregarEmpleado(empleado)
        messagebox.showinfo(
            "Empleado agregado", "El empleado se ha agregado exitosamente"
        )
        return funcion_manejo()

    # metodo para despedir a un empleado
    def _despedir(self, tipo_empleado: Literal["Mecanico", "Vendedor"], funcion_manejo: Callable[[], None]) -> None:
        nombre_empleado = self.field_frame.getValue(tipo_empleado)
        if tipo_empleado == "Mecanico":
            indx = next(
                (
                    i
                    for i, nombre in enumerate(
                        map(lambda e: e.getNombre(), self._parqueadero.getMecanicos())
                    )
                    if nombre == nombre_empleado
                )
            )
            empleado = self._parqueadero.getMecanicos()[indx]
            desicion = messagebox.askyesno(
                "¿Esta seguro?",
                f"¿Esta seguro que desea despedir a {empleado.getNombre()}?",
            )
            if desicion:
                self._parqueadero.getEmpleados().remove(empleado)
                messagebox.showinfo("Empleado despedido", "Empleado despedido")
                return funcion_manejo()
            else:
                return funcion_manejo()
        else:
            indx = next(
                (
                    i
                    for i, nombre in enumerate(
                        map(lambda e: e.getNombre(), self._parqueadero.getVendedores())
                    )
                    if nombre == nombre_empleado
                )
            )
            empleado = self._parqueadero.getVendedores()[indx]
            desicion = messagebox.askyesno(
                "¿Esta seguro?",
                f"¿Esta seguro que desea despedir a {empleado.getNombre()}?",
            )
            if desicion:
                self._parqueadero.getEmpleados().remove(empleado)
                messagebox.showinfo("Empleado despedido", "Empleado despedido")
                return funcion_manejo()
            else:
                return funcion_manejo()

    # ayudas para bonificaciones_...
    def _bonificaciones(self, funcion_manejo: Callable[[], None]) -> None:
        numero = self.field_frame.getValueNumero(
            "Minimo número de servicios para bonificación", int
        )
        porcentaje_salario = (
            self.field_frame.getValueNumero(
                "Porcentaje en que aumentara el salario", float
            )
            + 1
        )
        porcentaje_comision = (
            self.field_frame.getValueNumero(
                "Porcentaje en que aumentara la comisión", float
            )
            + 1
        )

        mecanicos_por_bonificar = filter(
            lambda m: m.getServiciosRealizados() > numero,
            self._parqueadero.getMecanicos(),
        )
        if not mecanicos_por_bonificar:
            messagebox.showinfo("No hay mecanicos", "No hay mecanicos por bonificar")
            return funcion_manejo()

        r = ""
        for mecanico in self._parqueadero.getMecanicos():
            salario_antes = mecanico.getSalario()
            nuevo_salario = salario_antes * porcentaje_salario
            mecanico.setSalario(nuevo_salario)
            comision_antes = mecanico.getComision()
            nueva_comision = comision_antes * porcentaje_comision
            mecanico.setComision(nueva_comision)
            r += f"{mecanico.getNombre}\nSalario: {salario_antes} -> {nuevo_salario}\nComisión: {comision_antes} -> {nueva_comision}\n"
        # mostrar r
        self.imprimir("Bonificaciones realizadas", r)
        return funcion_manejo()

    # agregar producto al almacen
    def _agregar_producto(self, funcion_manejo: Callable[[], None]) -> None:
        tipo_producto = TipoProducto[self.field_frame.getValue("Tipo de producto").upper()]
        estado = TipoEstado.EXCELENTE_ESTADO
        if self.field_frame.getValue("Estado") == "Buen estado":
            estado = TipoEstado.BUEN_ESTADO
        producto = Producto(tipo_producto, estado)
        self._parqueadero.getAlmacen().agregarProducto(producto)
        messagebox.showinfo("Agregado", "El producto ha sido agregado")
        return funcion_manejo()

    # agregar plazas
    def _plazas(self, funcion_manejo: Callable[[], None]) -> None:
        plazas_carro = self.field_frame.getValueNumero(
            "Plazas normales para carro", int
        )
        plazas_carro_discapacitados = self.field_frame.getValueNumero(
            "Plazas para condición de discapacidad", int
        )
        plazas_moto = self.field_frame.getValueNumero("Plazas normales para moto", int)
        plazas_moto_altocc = self.field_frame.getValueNumero(
            "Plazas para moto de altoCC", int
        )

        self._parqueadero.agregarPlazas(plazas_carro, False, "Carro")
        self._parqueadero.agregarPlazas(plazas_carro_discapacitados, True, "Carro")
        self._parqueadero.agregarPlazas(plazas_moto, False, "Moto")
        self._parqueadero.agregarPlazas(plazas_moto_altocc, False, "Moto altoCC")
        self.imprimir("Plazas agregadas:")
        self.imprimir(f"\t- {plazas_carro} plaza(s) normales para carro")
        self.imprimir(f"\t- {plazas_carro_discapacitados} plaza(s) para condición de discapacidad")
        self.imprimir(f"\t- {plazas_moto} plaza(s) normales para moto")
        self.imprimir(f"\t- {plazas_moto_altocc} plaza(s) para moto de altoCC")
        return funcion_manejo()

    # retirar un vehiculo
    def _retirar(self, funcion_manejo: Callable[[], None]) -> None:
        placa = self.field_frame.getValue("Placa")
        vehiculo = self._baseDatos.buscarVehiculoRegistrado(placa)
        if vehiculo is not None:
            dueno = vehiculo.getDueno()
            if dueno is not None:
                factura = dueno.getFactura()
                if factura is not None:
                    fecha_entrada = factura.getFecha()
                    hora_entrada = factura.getHoraIngreso()
                    fecha_salida = datetime.now().date()
                    hora_salida = datetime.now().time()
                    horas = (
                        datetime.combine(fecha_entrada, hora_entrada)
                        - datetime.combine(fecha_salida, hora_salida)
                    ).seconds / 3600
                    factura.agregarServicio("Parqueadero", horas)
                    self.imprimir("Su factura:\n" + str(factura))
                    dueno.setFactura(None)
                    self._parqueadero.retirarVehiculo(vehiculo.getPlaca())
                    self.imprimir("Vehiculo retirado, vuelve pronto :)")
                    return funcion_manejo()
        else:
            self.imprimir(
                "Error: El vehiculo no se encuentra en el parqueadero"
            )
            return funcion_manejo()

    # mostrar informacion de un cliente
    def _buscar_cliente(self, funcion_manejo: Callable[[], None]) -> None:
        cedula = self.field_frame.getValueNumero("Cédula", int)
        cliente = self._baseDatos.buscarClienteRegistrado(cedula)
        r = ""
        if cliente is not None:
            r += f"Nombre: {cliente.getNombre()}\nCédula: {str(cliente.getCedula())}\nCorreo: {cliente.getCorreo()}\nDirección: {cliente.getDireccion()}\nTeléfono: {str(cliente.getTelefono())}\n"
            if cliente.isDiscapacitado():
                r += "En condición de discapacidad: si\n"
            else:
                r += "En condición de discapacidad: no\n"
            if cliente.getFactura() is not None:
                r += f"Se ha generado la siguiente factura para este cliente:\n{cliente.getFactura()}"  # TODO: a donde ¿?¿?¿?¿?¿?
            messagebox.showinfo("Cliente", r)
            return funcion_manejo()
        else:
            messagebox.showerror("Error", "El cliente no se encuentra registrado")
            return funcion_manejo()

    # funcionalidades internas
    def _agregar_carro_venta(self, funcion_manejo: Callable[[], None]) -> None:
        self.field_frame.destroy()
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Placa", "Marca", "Color", "Modelo", "Tipo", "Puestos", "Precio"],
            "Valor",
            None,
            None,
            {
                "Marca": [m.name.title() for m in MarcasCarro],
                "Tipo": ["Mecanico", "Automatico"],
                "Color": ColoresVehiculo.lista()
            },
            titulo="Ingrese los datos del carro",
        )
        self.field_frame.pack()
        self.btn_principal.config(text="Agregar", command=lambda: self._agregar_carro(funcion_manejo))

    def _agregar_empleado(self, tipo_empleado: Literal["Mecanico", "Vendedor"], funcion_manejo: Callable[[], None]) -> None:
        self.field_frame.destroy()
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Cédula", "Nombre", "Tipo", "Teléfono", "Correo", "Dirección", "Salario"],
            "Valor",
            [None, None, tipo_empleado, None, None, None, None],
            ["Tipo"],
            titulo="Ingrese los datos del empleado",
        )
        self.field_frame.pack()
        self.btn_principal.config(
            text="Agregar", command=lambda: self._agregar(tipo_empleado, funcion_manejo)
        )

    def _despedir_empleado(
        self, tipo_empleado: Literal["Mecanico", "Vendedor"], funcion_manejo: Callable[[], None]
    ) -> None:
        self.field_frame.destroy()
        lista_empleados = self._parqueadero.getMecanicos()
        if tipo_empleado == "Vendedor":
            lista_empleados = self._parqueadero.getVendedores()
        lista_nombres_empleados = map(lambda e: e.getNombre(), lista_empleados)
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            [tipo_empleado],
            "Valor",
            None,
            None,
            {tipo_empleado: [*lista_nombres_empleados]},
            titulo="Ingrese la cédula del empleado",
        )
        self.field_frame.pack()
        self.btn_principal.config(
            text="Despedir", command=lambda: self._despedir(tipo_empleado, funcion_manejo)
        )

    def _estadisticas_mecanicos(self, funcion_manejo: Callable[[], None]) -> None:
        r = ""  # donde se va a mostrar esto??
        for mecanico in self._parqueadero.getMecanicos():
            r += f"{mecanico.getNombre()}\nCédula: {str(mecanico.getCedula())}\nSalario: {str(mecanico.getSalario())}\nComisión: {str(mecanico.getComision())}\nServicios realizados: {str(mecanico.getServiciosRealizados())}\n"
        messagebox.showinfo("Estadisticas de mecanicos", r)
        return funcion_manejo()

    def _bonificaciones_mecanicos(self, funcion_manejo: Callable[[], None]) -> None:
        self.field_frame.destroy()
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            [
                "Minimo número de servicios para bonificación",
                "Porcentaje en que aumentara el salario",
                "Porcentaje en que aumentara la comisión",
            ],
            "Valor",
            None,
            None,
            titulo="Bonificaciones mecanicos",
        )
        self.field_frame.pack()
        self.btn_principal.config(text="Continuar", command=lambda: self._bonificaciones(funcion_manejo))

    def _agregar_producto_almacen(self, funcion_manejo: Callable[[], None]) -> None:
        self.field_frame.destroy()
        tipos_producto = [p.name.title() for p in TipoProducto]
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Tipo de producto", "Estado"],
            "Valor",
            None,
            None,
            {
                "Tipo de producto": tipos_producto,
                "Estado": ["Excelente estado", "Buen estado"],
            },
            titulo="Agregar producto al almacén",
        )
        self.field_frame.pack()
        self.btn_principal.config(text="Agregar", command=lambda: self._agregar_producto(funcion_manejo))

    def _inventario_almacen(self, funcion_manejo: Callable[[], None]) -> None:
        almacen = self._parqueadero.getAlmacen()
        d: dict[str, int] = {}
        r = ""
        for producto in almacen.getInventario():
            if producto.getTipo().name.title() not in d:
                d[producto.getTipo().name.title()] = 1
            d[producto.getTipo().name.title()] += 1
        for key in d:
            r+= f"Tipo de producto:{key}\nExistencias: {d[key]}\n"
        messagebox.showinfo("Inventario", r)
        return funcion_manejo()

    def _agregar_plazas(self, funcion_manejo: Callable[[], None]) -> None:
        self.field_frame.destroy()
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            [
                "Plazas normales para carro",
                "Plazas para condición de discapacidad",
                "Plazas normales para moto",
                "Plazas para moto de altoCC",
            ],
            "Valor",
            None,
            None,
            titulo="Ingrese los números para cada caso, si no desea agregar en alguna ingrese '0'",
        )
        self.field_frame.pack()
        self.btn_principal.config(text="Agregar", command=lambda: self._plazas(funcion_manejo))

    def _retirar_vehiculo(self, funcion_manejo: Callable[[], None]) -> None:
        self.field_frame.destroy()
        vehiculos = filter(lambda e: e[1].estaParqueado(), self.getBaseDatos().getVehiculosRegistrados().items())
        placas = map(lambda e: e[1].getPlaca(), vehiculos)
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Placa"],
            "Valor",
            None,
            None,
            combobox={"Placa": list(placas)},
            titulo="Ingrese la placa del vehículo a retirar",
        )
        self.field_frame.pack()
        self.btn_principal.config(text="Retirar", command=lambda: self._retirar(funcion_manejo))

    def _informacion_cliente(self, funcion_manejo: Callable[[], None]) -> None:
        self.field_frame.destroy()
        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Cédula"],
            "Valor",
            None,
            None,
            titulo="Ingrese la cédula del cliente",
        )
        self.field_frame.pack()
        self.btn_principal.config(text="Buscar", command=lambda: self._buscar_cliente(funcion_manejo))
