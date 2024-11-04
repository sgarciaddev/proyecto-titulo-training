# Proyecto de título - ML Training

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
├── .env.example          # Archivo de ejemplo para las variables de entorno
├── .gitignore            # Archivo de configuración de git
├── requirements.txt      # Archivo de dependencias de Python
└── README.md             # Esta documentación
```

## Sets de datos

Por tamaño, los datasets no se encuentran presentes en el repositorio. Es 
por ello, que se necesita contar con ellos para configurar la variable de 
entorno `DATA_SOURCE_PATH` en el archivo `.env`. Toda la documentación 
referente a los sets de datos se encuentra en el archivo `README.md` dentro 
de la carpeta `ddosmllib/data/`, al que puedes acceder [aquí](ddosmllib/data/README.md).
