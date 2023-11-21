from typing import cast
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.parqueadero.producto  import Producto
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_estado import TipoEstado
from admon_parqueadero.gestorAplicacion.parqueadero.tipo_producto import TipoProducto
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.gestorAplicacion.personas.empleado import Empleado
from admon_parqueadero.gestorAplicacion.vehiculos.carro import Carro
from admon_parqueadero.gestorAplicacion.vehiculos.marcasCarro import MarcasCarro
from admon_parqueadero.gestorAplicacion.vehiculos.moto import Moto
from admon_parqueadero.gestorAplicacion.vehiculos.tipo_vehiculo import TipoVehiculo
from admon_parqueadero.gestorAplicacion.vehiculos.vehiculo import Vehiculo

class GenerarDatos:
    def __init__(self, baseDatos: BaseDatos) -> None:
        self._base_datos = baseDatos
        if not baseDatos.datosDePruebaGenerados:
            self._crear_datos()

    def _crear_datos(self) -> None:
        parqueadero = self._base_datos.getParqueadero()
        clientes = [Cliente("Georgia Hodges", 88282864, 8822435588, "odio.tristique@protonmail.ca", "P.O. Box 837, 1931 Faucibus Road", False),
                Cliente("Ashton Buckner", 97216432, 4784015772, "quisque.ac.libero@outlook.couk", "610-489 Sodales Street", False),
                Cliente("Eaton Gutierrez", 79618030, 8782786843, "arcu.ac.orci@icloud.net", "Ap #376-1454 Semper Avenue", False),
                Cliente("Benedict Wyatt", 13251063, 4554518795, "cursus.vestibulum@hotmail.edu", "P.O. Box 189, 2706 Nibh. Road", False),
                Cliente("Warren Watson", 28546557, 5366791828, "metus.vitae@icloud.com", "901-8274 Convallis Av.", False),
                Cliente("Rigel Cleveland", 10351169, 6582360165, "varius.orci@yahoo.org", "Ap #269-8928 Aliquam Ave", False),
                Cliente("Holly Barry", 77363835, 3338525656, "risus.morbi@aol.couk", "Ap #988-3255 Gravida. St.", True),
                Cliente("Abbot English", 24694603, 4879434732, "morbi.tristique@icloud.net", "Ap #118-8902 Semper. Street", False)]
        
        empleados = [ Empleado("Belle Nolan", 53799227, 2363874677, "imperdiet.erat@hotmail.net", "P.O. Box 371, 4784 Nunc Rd.", "Vendedor", 1465938),
                Empleado("Addison Hobbs", 34149111, 3840124676, "gravida.nunc.sed@google.net", "Ap #179-7256 Iaculis, Ave", "Vendedor", 1737354),
                Empleado("Elton Carroll", 38543024, 7261237929, "egestas@google.org", "P.O. Box 717, 9254 Mi Rd.", "Mecanico", 1942580),
                Empleado("Emery Whitehead", 21372067, 7528886123, "tincidunt@icloud.org", "8875 Est, Ave", "Vendedor", 1155662),
                Empleado("Joelle Combs", 26943851, 7718662286, "cras.vehicula@google.com", "885-4962 Dapibus St.", "Mecanico", 1062081),
                Empleado("Ira Lynn", 52682220, 4148814432, "suscipit.est@google.net", "444-6842 Auctor Rd.", "Vendedor", 1811143),
                Empleado("Angelica Olsen", 63772800, 7852724044, "dui.fusce.diam@icloud.net", "P.O. Box 804, 7026 Sodales. Road", "Mecanico", 1957091),
                Empleado("Tashya Floyd", 38868093, 7958533122, "quam.vel@aol.couk", "Ap #371-9085Posuere St.", "Vendedor", 1400694),
                Empleado("Iona Gordon", 46243263, 1489760813, "massa.mauris@icloud.org", "Ap #668-702 Magna. Av.", "Vendedor", 1448290),
                Empleado("Lareina Wilkinson", 53388926, 3735464647, "odio@yahoo.org", "6399 Rutrum St.", "Mecanico", 1582047),
                Empleado("Kai Miles", 66207025, 5255067054, "semper.rutrum@hotmail.couk", "992-5371 Mauris Ave", "Mecanico", 1106243),
                Empleado("Paki Hill", 63116666, 8541572636, "lacinia.at@icloud.org", "P.O. Box 772, 3895 Aliquet Ave", "Mecanico", 1184994)]
        
        productos: list[Producto] = [Producto(TipoProducto.TRANSMISION, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.TRANSMISION, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.TRANSMISION, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.LIQUIDOS, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.LIQUIDOS, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LIQUIDOS, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LIQUIDOS, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.LIQUIDOS, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LIQUIDOS, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LIQUIDOS, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LIQUIDOS, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.TRANSMISION, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.TRANSMISION, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.TRANSMISION, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.TRANSMISION, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.TRANSMISION, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.TRANSMISION, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACEITE, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.CADENA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.TRANSMISION, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.AMORTIGUADOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.PEDALES, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.MOTOR, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.RIN, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.LLANTA, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.BATERIA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.ACELERADOR, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.GASOLINA, TipoEstado.EXCELENTE_ESTADO),
        		Producto(TipoProducto.FRENO, TipoEstado.BUEN_ESTADO),
        		Producto(TipoProducto.PEDAL, TipoEstado.BUEN_ESTADO)]
        
        carros_venta: list[Carro] = [Carro("ILQ380", None, MarcasCarro.KIA.name.title(), "Azul", "2023", TipoVehiculo.MECANICO, 5, True, 20000000),
                Carro("EBU624", None, MarcasCarro.TOYOTA.name.title(), "Rojo", "2012", TipoVehiculo.MECANICO, 5, True, 30000000),
                Carro("HMK074", None, MarcasCarro.CHEVROLET.name.title(), "Negro", "2010", TipoVehiculo.AUTOMATICO, 5, True, 25000000),
                Carro("ILQ380", None, MarcasCarro.KIA.name.title(), "Azul", "2003", TipoVehiculo.MECANICO, 5, False, 50000000),
                Carro("JVV624", None, MarcasCarro.RENAULT.name.title(), "Amarillo", "2012", TipoVehiculo.MECANICO, 5, True, 33000000),
                Carro("AGDK074", None, MarcasCarro.RENAULT.name.title(), "Gris", "2020", TipoVehiculo.AUTOMATICO, 5, False, 45000000),
                Carro("BVC480", None, MarcasCarro.KIA.name.title(), "Azul", "2023", TipoVehiculo.MECANICO, 5, True, 60000000),
                Carro("EVU724", None, MarcasCarro.MAZDA.name.title(), "Negro", "2022", TipoVehiculo.MECANICO, 5, True, 70000000),
                Carro("HAK054", None, MarcasCarro.CHEVROLET.name.title(), "Negro", "2020", TipoVehiculo.AUTOMATICO, 5, False, 65000000),
                Carro("AQE335", None, MarcasCarro.MAZDA.name.title(), "Verde", "2018", TipoVehiculo.MECANICO, 5, False, 70000000)]
        
        vehiculos_clientes: list[Vehiculo] = [Carro("LCX368", clientes[6], MarcasCarro.MAZDA.name.title(), "Negro", "2020", TipoVehiculo.MECANICO, 5, clientes[6].isDiscapacitado()),
                Moto("LOR31V", clientes[4], MarcasCarro.KIA.name.title(), "Azul", "2011", TipoVehiculo.NORMAL, 174),
                Moto("YOQ05B", clientes[3], MarcasCarro.KIA.name.title(), "Azul", "2016", TipoVehiculo.ALTOCC, 82),
                Carro("YCI195", clientes[3], MarcasCarro.CHEVROLET.name.title(), "Azul", "2023", TipoVehiculo.AUTOMATICO, 5, clientes[3].isDiscapacitado()),
                Carro("ISZ049", clientes[3], MarcasCarro.MAZDA.name.title(), "Verde", "2022", TipoVehiculo.AUTOMATICO, 5, clientes[3].isDiscapacitado()),
                Moto("TZL87N", clientes[0], MarcasCarro.MAZDA.name.title(), "Azul", "2015", TipoVehiculo.NORMAL, 109),
                Moto("LCI31H", clientes[5], MarcasCarro.TOYOTA.name.title(), "Rojo", "2017", TipoVehiculo.NORMAL, 112),
                Carro("WOV536", clientes[7], MarcasCarro.KIA.name.title(), "Gris", "2014", TipoVehiculo.MECANICO, 5, clientes[7].isDiscapacitado()),
                Carro("TAU635", clientes[4], MarcasCarro.RENAULT.name.title(), "Gris", "2011", TipoVehiculo.AUTOMATICO, 5, clientes[4].isDiscapacitado()),
                Carro("RKX138", clientes[4], MarcasCarro.TOYOTA.name.title(), "Azul", "2011", TipoVehiculo.MECANICO, 5, clientes[4].isDiscapacitado()),
                Carro("RSF358", clientes[2], MarcasCarro.KIA.name.title(), "Verde", "2011", TipoVehiculo.AUTOMATICO, 5, clientes[2].isDiscapacitado()),
                Carro("VUJ819", clientes[6], MarcasCarro.RENAULT.name.title(), "Rojo", "2020", TipoVehiculo.MECANICO, 5, clientes[6].isDiscapacitado()),
                Carro("BTV358", clientes[2], MarcasCarro.KIA.name.title(), "Gris", "2021", TipoVehiculo.AUTOMATICO, 5, clientes[2].isDiscapacitado()),
                Moto("VLC37F", clientes[2], MarcasCarro.KIA.name.title(), "Verde", "2019", TipoVehiculo.ALTOCC, 124),
                Carro("FPZ394", clientes[6], MarcasCarro.TOYOTA.name.title(), "Gris", "2022", TipoVehiculo.AUTOMATICO, 5, clientes[6].isDiscapacitado()),
                Moto("VHD89N", clientes[5], MarcasCarro.KIA.name.title(), "Azul", "2010", TipoVehiculo.NORMAL, 99)]
        
        for cliente in clientes:
            self._base_datos.registrarCliente(cliente)
        if parqueadero is not None:
            for empleado in empleados:
                parqueadero.agregarEmpleado(empleado)
            for producto in productos:
                parqueadero.getAlmacen().agregarProducto(producto)
            for carro in carros_venta:
                parqueadero.agregarVehiculoVenta(carro)
            for vehiculo in vehiculos_clientes: # TODO: se deben ingresar los vehiculos al parqueadero y generar la factura
                self._base_datos.registrarVehiculo(vehiculo)
                dueno = vehiculo.getDueno()
                if dueno is not None:
                    dueno.agregarVehiculo(vehiculo)
                    if vehiculo.getPlaca() in ["LCX368", "ISZ049", "TAU635", "RSF358", "VUJ819"]:
                        if dueno.isDiscapacitado():
                            for p in parqueadero.getPlazas():
                                if p.isDiscapacitado() and p.getEstado() == "Disponible" and p.getTipo() == "Carro":
                                    parqueadero.ingresarVehiculo(vehiculo, p)
                                    factura = dueno.getFactura()
                                    if factura is not None:
                                        factura.agregarServicio("Parqueadero", 1)
                                        break
                        else:
                            for p in parqueadero.getPlazas():
                                if p.getEstado() == "Disponible" and p.getTipo() == "Carro" and not p.isDiscapacitado():
                                    parqueadero.ingresarVehiculo(vehiculo, p)
                                    factura = dueno.getFactura()
                                    if factura is not None:
                                        factura.agregarServicio("Parqueadero", 1)
                                        break
                    
                    else:
                        if vehiculo.getPlaca() in ["LOR31V", "TZL87N", "VLC37F"]:
                            if cast(Moto, vehiculo).getTipo() == TipoVehiculo.ALTOCC:
                                for p in parqueadero.getPlazas():
                                    if p.getTipo() == "Moto altoCC" and p.getEstado() == "Disponible":
                                        parqueadero.ingresarVehiculo(vehiculo, p)
                                        factura = dueno.getFactura()
                                        if factura is not None:
                                            factura.agregarServicio("Parqueadero", 1)
                                            break
                            else:
                                for p in parqueadero.getPlazas():
                                    if p.getTipo() == "Moto" and p.getEstado() == "Disponible":
                                        parqueadero.ingresarVehiculo(vehiculo, p)
                                        factura = dueno.getFactura()
                                        if factura is not None:
                                            factura.agregarServicio("Parqueadero", 1)
                                            break
                      
        admin = Empleado("Guzman", 123, 310111111, "guzman@unal.edu.co", "P.O. Box 837, 1931 Faucibus Road", "Administrador", 3000000)
        if parqueadero is not None:
            parqueadero.setAdministrador(admin)
