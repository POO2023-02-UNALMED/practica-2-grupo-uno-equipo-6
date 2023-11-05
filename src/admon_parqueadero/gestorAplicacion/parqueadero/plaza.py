from gestorAplicacion.vehiculos import Vehiculo;
import pickle
plazasTotales  = []
class Plaza (pickle):
    numeroPlaza = 0
    discapacitado = False #Si es una plaza para clientes discapacitados o no
    estado = ""  #Disponible u ocupado
    vehiculo = Vehiculo() # El vehículo que lo está ocupando
    tipo = "" #Si es de tipo carro o moto
    
	# private static List<Plaza> plazasTotales = new ArrayList<Plaza>();
	
    def __init__(self,numeroPlaza,discapacitado,estado, vehi,  tipo):
        self.numeroPlaza = numeroPlaza
        self.discapacitado = discapacitado
        self.estado = estado
        self.vehiculo = vehi;
        self.tipo = tipo;
        plazasTotales.append(self);

    def setDiscapacitado(self,disc):
        self.discapacitado = disc

    def getDiscapacitado(self):
        return self.discapacitado


    def setNumeroPlaza(self, numeroP) :
        self.numeroPlaza = numeroP

    def getNumeroPlaza(self) :
        return self.numeroPlaza


    def setEstado(self,estado) :
        self.estado = estado

    def getEstado(self) :
        return self.estado


    def setVehiculo(self,vehi) :
        self.vehiculo = vehi


    def getVehiculo(self) :
        return self.vehiculo


    def getTipo(self) :
        return self.tipo


    def setTipo(self,tipo) :
        self.tipo = tipo
