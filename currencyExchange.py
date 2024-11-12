import requests

def currency_exchange():
    amount = float(input("Enter the amount you want to convert:"))
    source_currency = input("Enter the source currency: ").upper()
    target_currency = input("Enter the target currency: ").upper()
    
    api_key = "b2a94afbe7084b65d77830c2"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{source_currency}"

    
    response = requests.get(url)
    
    if (response.status_code == 200):
        data = response.json()
        conversion_rates = data.get("conversion_rates", {})
        
        if target_currency in conversion_rates:
            exchange_rate = conversion_rates[target_currency]
            converted_amount = exchange_rate * amount 
            print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}.")
    else:
        print("API request invalid! Please check the API key or internet connection.")
        
        
currency_exchange()