from os import getenv, listdir
from os.path import join as join_path, isfile
from enum import Enum
from dotenv import load_dotenv
from pandas import read_parquet

# Se cargan las variables de entorno (.env). En caso de que no existan, se lanza una excepción
load_dotenv()
if not getenv('DATA_SOURCE_PATH'):
    raise EnvironmentError('La variable de entorno DATA_SOURCE_PATH no esta definida')
if not getenv('TRAINED_MODELS_PATH'):
    raise EnvironmentError('La variable de entorno TRAINED_MODELS_PATH no esta definida')
if not getenv('SAVED_PARQUET_PATH'):
    raise EnvironmentError('La variable de entorno SAVED_PARQUET_PATH no esta definida')

class ArchivoProyecto(Enum):
    """
    Enumeración de los archivos de datos del proyecto
    """
    DATOS: str = 'DATA_SOURCE_PATH'
    MODELOS_ENTRENADOS: str = 'TRAINED_MODELS_PATH'
    ARCHIVOS_GUARDADOS: str = 'SAVED_PARQUET_PATH'


class DatasetProyecto(Enum):
    """
    Enumeración de los datasets del proyecto
    """
    CIC_DDoS2019: str = 'cic-ddos2019'
    N_BaIoT_RF: str = 'nbaiot-rf'
    N_BaIoT_XGB: str = 'nbaiot-xgb'


def get_dataset_df(dataset: DatasetProyecto):
    """
    Listar los archivos de un dataset
    :param dataset: DatasetProyecto a listar
    :return: DataFrame con los datos del dataset
    """
    dataset_path = join_path(getenv(ArchivoProyecto.ARCHIVOS_GUARDADOS.value),
                             f'{dataset.value}.parquet')
    if not isfile(dataset_path):
        raise FileNotFoundError(f'El dataset {dataset.value} no esta registrado')
    return read_parquet(dataset_path)