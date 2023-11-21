#Funcionalidad del módulo: contiene la clase Serializador, 
#esta sirve para escribir los datos que se desean guardar 
#en la base de datos. Se utilizó pickle.
#Componentes del módulo: Serializador.
#Autores: Sofia, Sara, Alejandro, Sebastián, Katherine


from pathlib import Path
import pickle

from admon_parqueadero.baseDatos.baseDatosException import BaseDatosException


class Serializador:
    def __init__(self) -> None:
        pass

    def escribirObjeto(self, objeto: object, ruta: Path) -> None:
        if not ruta.exists():
            self._crearArchivo(ruta)

        try:
            with ruta.open("wb") as archivo:
                pickle.dump(objeto, archivo)
        except (IOError, pickle.PicklingError) as e:
            raise BaseDatosException(
                "Ha ocurrido un error al escribir el archivo", e
            ) from e

    def _crearArchivo(self, ruta: Path) -> None:
        if not ruta.parent.exists():
            ruta.parent.mkdir(parents=True)
        with open(ruta, "wb"):
            pass
