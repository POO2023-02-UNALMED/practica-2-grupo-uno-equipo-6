#Funcionalidad del módulo: contiene la clase Deserializador, 
#esta sirve para leer los datos que están guardados en la
#base de datos. Se utilizó pickle para esto.
#Componentes del módulo:  Deserializador
#Autores: Sofia, Sara, Alejandro, Sebastián, Katherine



from pathlib import Path
import pickle

from admon_parqueadero.baseDatos.baseDatosException import BaseDatosException


class Deserializador:
    def __init__(self, ruta: Path) -> None:
        self._ruta = ruta

    def leerObjeto(self) -> object:
        if not self._ruta.exists():
            return None

        try:
            with self._ruta.open("rb") as archivo:
                objeto = pickle.load(archivo)
                return objeto
        except (IOError, pickle.UnpicklingError) as e:
            raise BaseDatosException(
                "Ha ocurrido un error leyendo el archivo", e
            ) from e

    def existenDatos(self) -> bool:
        return self._ruta.exists()
