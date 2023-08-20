# API Key from https://manage.exchangeratesapi.io/dashboard 
# 35a5ee5b6724755185ecebb3d17a754c

import requests

API_KEY = "35a5ee5b6724755185ecebb3d17a754c"
BASE_URL = "http://api.exchangeratesapi.io/v1/"
PARAMS = {'access_key': API_KEY}

try:
    response = requests.get(BASE_URL, params=PARAMS, timeout=100)
    response.raise_for_status()
    data = response.json()

    exchange_rates = data['rates']

    amount = float(input("Enter amount: "))
    source_currency = input("Enter source currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., EUR): ").upper()

    if source_currency in exchange_rates and target_currency in exchange_rates:
        source_rate = exchange_rates[source_currency]
        target_rate = exchange_rates[target_currency]

        converted_amount = amount * (target_rate / source_rate)
        print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Invalid currency code.")

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")