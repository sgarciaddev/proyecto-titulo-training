from os import getenv
from os.path import join as join_path, isfile
from pandas import read_csv, DataFrame
from dotenv import load_dotenv

class EnvVarNotDefinedError(Exception):
    pass

load_dotenv()
if not getenv('DATA_SOURCE_PATH'):
    raise EnvVarNotDefinedError('Environment variable DATASOURCE_PATH not defined')
if not getenv('TRAINED_MODELS_PATH'):
    raise EnvVarNotDefinedError('Environment variable OUT_MODELS_PATH not defined')

def get_dataset_fullpath(*args: str) -> str:
    """
    Permite obtener la ruta completa de un archivo de datos
    :param args: Ruta del dataset a obtener
    :return: Ruta completa del dataset
    """
    ds_path = getenv('DATA_SOURCE_PATH')
    fullpath = join_path(ds_path, *args)
    return fullpath

def get_dataset_df(*args: str) -> DataFrame:
    """
    Permite obtener un DataFrame de un archivo de datos
    :param args: Ruta del dataset a obtener
    :return: DataFrame del dataset, si existe, de lo contrario None
    :raises FileNotFoundError: Si el archivo no existe
    """
    ds_fullpath = get_dataset_fullpath(*args)
    if not isfile(f'{ds_fullpath}.csv'):
        raise FileNotFoundError(f'Dataset `{args[-1]}` from `{args[0]}` not found')
    return read_csv(f'{get_dataset_fullpath(*args)}.csv', low_memory=False)
