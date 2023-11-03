# ETL Script: Extracción y Carga de Datos en Redshift

Este proyecto consiste en un script de extracción y carga de datos que obtiene información de una API pública y la almacena en una tabla en Amazon Redshift. En este ejemplo, se utiliza la API de BlueLytics que proporciona datos de tipos de cambio en Argentina.

## Objetivo

El objetivo principal de este proyecto es proporcionar un script ETL inicial que permita la extracción de datos de una API y su carga en Redshift. El script se encarga de:

- Realizar una solicitud a una API pública.
- Procesar y transformar los datos.
- Crear una tabla en Redshift.
- Cargar los datos en la tabla.

# Extracción y Carga de Datos en Redshift desde una API Externa

Este proyecto se enfoca en la extracción de datos de una API externa y su carga en una tabla de Amazon Redshift. El objetivo principal es obtener datos financieros de la API y almacenarlos en una tabla en Redshift para su posterior análisis.

## Archivos y Módulos

### 1. `main.py`
Script principal que ejecuta la lógica de extracción, transformación y carga de datos. Utiliza módulos separados para la conexión a Redshift y la lógica de la API.

### 2. `api_handler.py`
Módulo que contiene la lógica de extracción de datos desde la API externa.

### 3. `redshift_handler.py`
Módulo que maneja la conexión a Redshift, la creación de la tabla y la carga de datos.

### 4. `.env`
El archivo `.env` contiene las variables de entorno necesarias para el proyecto, como las credenciales de Redshift y la URL de la API.

## Variables del Archivo .env

- `API_URL`: URL de la API externa que proporciona los datos financieros.
- `REDSHIFT_HOST`: Host de la instancia de Redshift.
- `REDSHIFT_PORT`: Puerto de la instancia de Redshift.
- `REDSHIFT_DB`: Nombre de la base de datos en Redshift.
- `REDSHIFT_USER`: Usuario para la conexión a Redshift.
- `REDSHIFT_PASSWORD`: Contraseña para la conexión a Redshift.

## Ejecución del Script

1. Asegúrate de tener instaladas las bibliotecas requeridas. Puedes usar `pip install -r requirements.txt` para instalarlas desde el archivo `requirements.txt`.
2. Configura las variables en el archivo `.env` con la información correspondiente.
3. Ejecuta el script `main.py` para iniciar la extracción y carga de datos en Redshift.
