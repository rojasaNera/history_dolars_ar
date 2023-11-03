import os

from flask.cli import load_dotenv
from api_handler import fetch_exchange_data, extract_exchange_rates
from redshift_handler import create_redshift_table, upload_to_redshift

def main():
    load_dotenv(".env")
    
    # URL de la nueva API pública
    api_url = os.environ.get("API_URL")
    
     # Extraer datos de la API
    data = fetch_exchange_data(api_url)
    
    # Transformar los datos relevantes
    exchange_rates = extract_exchange_rates(data)

    # Crear la tabla en Redshift
    create_redshift_table()
    
    # Cargar datos en Redshift
    upload_to_redshift(exchange_rates, "exchange_rates")

if __name__ == "__main__":
    main()
