# Proyecto de título - ML Training

<div align="center">

[![Python 3.10][python-badge]][python-web]
[![Virtualenv][venv-badge]][venv-web]
[![PyCharm][pycharm-badge]][pycharm-web]
[![Jupyter][jupyter-badge]][jupyter-web]

</div>

Repositorio de código con los algoritmos de entrenamiento de modelos de 
aprendizaje automático y profundo, en el contexto de desarrollo de la 
investigación *"Detección y mitigación de ataques DDoS en ambientes IoT/Cloud 
usando ML/DL"*.

## Prerequisitos

- Python 3.10 - venv e instalar `requirements.txt`, presente en la base del 
proyecto.
- Crear archivo .env con las variables de entorno:

    ```
    DATA_SOURCE_PATH="/ruta/a/los/datasets"
    TRAINED_MODELS_PATH="/ruta/modelos/entrenados"
    
    ```

- Tener disponible ambiente para trabajar con notebooks Jupyter. PyCharm ya 
  lo trae integrado, y existen extensiones para Visual Studio Code.

## Estructura de directorios

```
.
├── ddosmllib/            # Librería interna de funciones
│   └── data/
│       └── README.md     # Documentación de los datasets disponibles
├── jupyter/              # Notebooks de experimentación
├── out/                  # Modelos entrenados almacenados
├── saved/                # Sets de datos a rescatar para entrenamiento
├── .env.example          # Archivo de ejemplo para las variables de entorno
├── .gitignore            # Archivo de configuración de git
├── requirements.txt      # Archivo de dependencias de Python
└── README.md             # Esta documentación
```

> [!IMPORTANT]  
> La carpeta `out/` es donde se almacenan los modelos entrenados, y `saved/` 
> es donde se almacenan los sets de datos a utilizar. Ambas carpetas deben 
> existir, pero no se suben al repositorio para evitar problemas de espacio.

## Sets de datos

Por tamaño, los datasets no se encuentran presentes en el repositorio. Es 
por ello, que se necesita contar con ellos para configurar la variable de 
entorno `DATA_SOURCE_PATH` en el archivo `.env`. Toda la documentación 
referente a los sets de datos se encuentra en el archivo `README.md` dentro 
de la carpeta `ddosmllib/data/`, al que puedes acceder [aquí](ddosmllib/data/README.md).

[python-badge]: https://img.shields.io/badge/Python%203.10-3776AB?logo=python&logoColor=FFF&style=flat

[python-web]: https://www.python.org/

[venv-badge]: https://img.shields.io/badge/Virtualenv-4B8BBE?logo=python&logoColor=FFF&style=flat

[venv-web]: https://virtualenv.pypa.io/en/latest/

[pycharm-badge]: https://img.shields.io/badge/PyCharm-000?logo=pycharm&logoColor=FFF&style=flat

[pycharm-web]: https://www.jetbrains.com/pycharm/

[jupyter-badge]: https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=FFF&style=flat

[jupyter-web]: https://jupyter.org/
```