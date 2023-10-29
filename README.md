# ETL Script: Extracción y Carga de Datos en Redshift

Este proyecto consiste en un script de extracción y carga de datos que obtiene información de una API pública y la almacena en una tabla en Amazon Redshift. En este ejemplo, se utiliza la API de BlueLytics que proporciona datos de tipos de cambio en Argentina.

## Objetivo

El objetivo principal de este proyecto es proporcionar un script ETL inicial que permita la extracción de datos de una API y su carga en Redshift. El script se encarga de:

- Realizar una solicitud a una API pública.
- Procesar y transformar los datos.
- Crear una tabla en Redshift.
- Cargar los datos en la tabla.

## Archivos del Proyecto

- `etl_script.py`: Este archivo contiene el script en Python que realiza la extracción, transformación y carga de datos. Utiliza bibliotecas como `requests`, `pandas`, `psycopg2`, y `dotenv` para gestionar la configuración.

- `.env`: Un archivo que almacena las variables de entorno, incluyendo la URL de la API, las credenciales de Redshift y otros valores de configuración.

- `create_table.sql`: Un archivo SQL que contiene la consulta para crear la tabla en Redshift. Define la estructura de la tabla y la clave de ordenamiento.

## Variables en el Archivo .env

Asegúrate de configurar el archivo `.env` con las siguientes variables:

- `API_URL`: La URL de la API pública que deseas utilizar.
- `REDSHIFT_HOST`: El host de tu instancia de Redshift.
- `REDSHIFT_PORT`: El puerto de Redshift (suele ser 5439).
- `REDSHIFT_DB`: El nombre de la base de datos en Redshift.
- `REDSHIFT_USER`: Tu nombre de usuario de Redshift.
- `REDSHIFT_PASSWORD`: Tu contraseña de Redshift.

## Cómo Ejecutar el Script

Sigue estos pasos para ejecutar el script:

1. Clona o descarga este repositorio en tu máquina local.

2. Crea un archivo `.env` en la raíz del proyecto y configura las variables de entorno según tus necesidades.

3. Asegúrate de tener Python y las bibliotecas necesarias instaladas (puedes usar `pip install -r requirements.txt` para instalar las bibliotecas).

4. Ejecuta el script Python `etl_script.py` usando el intérprete de Python.

    ```
    python etl_script.py
    ```

5. El script obtendrá datos de la API, procesará la información y la almacenará en la tabla de Redshift.