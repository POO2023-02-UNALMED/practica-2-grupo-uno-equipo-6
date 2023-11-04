class Persona:
    def __init__(self, nombre: str, cedula: int, telefono: int, correo: str, direccion: str) -> None:
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono
        self._correo = correo
        self._direccion = direccion

    def setNombre(self, nombre: str) -> None:
        self._nombre = nombre

    def getNombre(self) -> str:
        return self._nombre

    def setCedula(self, cedula: int) -> None:
        self._cedula = cedula

    def getCedula(self) -> int:
        return self._cedula

    def setTelefono(self, telefono: int) -> None:
        self._telefono = telefono

    def getTelefono(self) -> int:
        return self._telefono
    
    def setCorreo(self, correo: str) -> None:
        self._correo = correo

    def getCorreo(self) -> str:
        return self._correo

    def setDireccion(self, direccion: str) -> None:
        self._direccion = direccion

    def getDireccion(self) -> str:
        return self._direccion
    