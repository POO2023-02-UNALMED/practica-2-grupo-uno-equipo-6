#Funcionalidad del módulo: contiene la clase BaseDatosException que hereda de Exception, 
#esta sirve para manejar errores relacionados a la base de datos.
#Componentes del módulo: BaseDatosException
#Autores: Sofia, Sara, Alejandro, Sebastián, Katherine


class BaseDatosException(Exception):
    def __init__(self, mensaje: str, causa: Exception) -> None:
        self._causa = causa
        super().__init__(mensaje)
