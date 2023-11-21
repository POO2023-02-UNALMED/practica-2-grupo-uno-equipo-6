class ErrorAplicacion(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(f"Manejo de errores de la aplicacion: {msg}")


class ErrorUsuario(ErrorAplicacion):
    def __init__(self, msg: str) -> None:
        super().__init__(f"error de usuario: {msg}")


class ErrorNumeroEsperado(ErrorUsuario):
    def __init__(self, msg: str) -> None:
        super().__init__(f"se esperaba un número para el valor de: {msg}")


class ErrorValorEsperado(ErrorUsuario):
    def __init__(self, msg: str) -> None:
        super().__init__(f"el valor para {msg} no puede estar vacío")


class ErroresVacios(ErrorUsuario):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class ErrorObjeto(ErrorAplicacion):
    def __init__(self, msg: str) -> None:
        super().__init__(f"error de objeto: {msg}")


class ErrorObjetoVacio(ErrorObjeto):
    def __init__(self, msg: str) -> None:
        super().__init__(f"el objeto {msg} se ecuentra vacio")


class ErrorLogicaIncorrecta(ErrorObjeto):
    def __init__(self, msg: str) -> None:
        super().__init__(f"logica incorrecta: {msg}")


class ErrorObjetoInexistente(ErrorObjeto):
    def __init__(self, msg: str) -> None:
        super().__init__(f"objeto no encontrado: {msg}")
