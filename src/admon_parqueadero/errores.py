class ErrorAplicacion(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(f"Manejo de errores de la aplicacion: {msg}")


class ErrorUsuario(ErrorAplicacion):
    def __init__(self, msg: str) -> None:
        super().__init__(f"Error de tipo: {msg}")


class ErrorNumeroEsperado(ErrorUsuario):
    def __init__(self, msg: str) -> None:
        super().__init__(f"se esperaba un número para el valor de: {msg}")
