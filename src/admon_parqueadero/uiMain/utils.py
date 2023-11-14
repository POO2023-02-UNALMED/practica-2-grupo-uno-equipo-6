from importlib.abc import Traversable
from importlib.resources import files


def ruta_imagen(imagen: str) -> Traversable:
    return ruta_imagenes().joinpath(imagen)


def ruta_imagenes() -> Traversable:
    return files("admon_parqueadero").joinpath("imagenes")