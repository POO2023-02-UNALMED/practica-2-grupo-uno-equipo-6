from pathlib import Path
import pickle

from admon_parqueadero.baseDatos.baseDatosException import BaseDatosException


class Deserializador:
    def __init__(self, ruta: Path) -> None:
        self._ruta = ruta

    def leerObjeto(self) -> object:
        try:
            with self._ruta.open("rb") as archivo:
                objeto = pickle.load(archivo)
                return objeto
        except pickle.UnpicklingError as e:
            raise BaseDatosException(
                "Ha ocurrido un error leyendo el archivo", e
            ) from e

    def existenDatos(self) -> bool:
        try:
            return self._ruta.stat().st_size == 0
        except FileNotFoundError:
            return True
