class BaseDatosException(Exception):
    def __init__(self, mensaje: str, causa: Exception) -> None:
        self._causa = causa
        super().__init__(mensaje)
