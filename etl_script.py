import os
import requests
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv(".env")

# URL de la nueva API pública
api_url = os.environ.get("API_URL")

# Realizar una solicitud a la API y obtener los datos en formato JSON
response = requests.get(api_url)
data = response.json()

# Extraer los datos de "oficial" y "blue"
oficial_data = data.get("oficial")
blue_data = data.get("blue")

# Configuración de la conexión a Redshift desde el archivo .env
redshift_host = os.environ.get("REDSHIFT_HOST")
redshift_port = os.environ.get("REDSHIFT_PORT")
redshift_db = os.environ.get("REDSHIFT_DB")
redshift_user = os.environ.get("REDSHIFT_USER")
redshift_password = os.environ.get("REDSHIFT_PASSWORD")

# Crear una conexión a Redshift
conn = psycopg2.connect(
    host=redshift_host,
    port=redshift_port,
    dbname=redshift_db,
    user=redshift_user,
    password=redshift_password
)

# Crear un DataFrame de Pandas con los datos de "oficial" y "blue"
oficial_df = pd.DataFrame({
    'fecha': pd.to_datetime(data['last_update']).date(),
    'value_avg': oficial_data['value_avg'],
    'value_sell': oficial_data['value_sell'],
    'value_buy': oficial_data['value_buy'],
    'currency_type': 1,
    'currency_name': 'Oficial'
})

blue_df = pd.DataFrame({
    'fecha': pd.to_datetime(data['last_update']).date(),
    'value_avg': blue_data['value_avg'],
    'value_sell': blue_data['value_sell'],
    'value_buy': blue_data['value_buy'],
    'currency_type': 2,
    'currency_name': 'Blue'
})

# Concatenar los DataFrames
exchange_rates_df = pd.concat([oficial_df, blue_df])

# Escribir los datos en Redshift
exchange_rates_df.to_sql("exchange_rates", conn, if_exists="replace", index=False)

# Cerrar la conexión a Redshift
conn.close()
