import requests
from datetime import datetime

def fetch_exchange_data(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data

def extract_exchange_rates(data):
    oficial_data = data.get("oficial")
    blue_data = data.get("blue")
    
    oficial_date = datetime.fromisoformat(data['last_update']).date()
    blue_date = oficial_date  # As both 'oficial' and 'blue' have the same 'last_update' date

    return [
        {'fecha': oficial_date, 'value_avg': oficial_data['value_avg'], 'value_sell': oficial_data['value_sell'],
         'value_buy': oficial_data['value_buy'], 'currency_type': 1, 'currency_name': 'Oficial'},
        {'fecha': blue_date, 'value_avg': blue_data['value_avg'], 'value_sell': blue_data['value_sell'],
         'value_buy': blue_data['value_buy'], 'currency_type': 2, 'currency_name': 'Blue'}
    ]
