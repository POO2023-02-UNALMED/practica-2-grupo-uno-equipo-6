from tkinter import messagebox


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
        messagebox.showerror("Error valores esperados", f"Los siguienstes campos no pueden estar vacios:{msg}")
