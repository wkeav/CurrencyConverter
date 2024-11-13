import requests

class Currency_converter:
    def __init__(self):
        self.amount = float(input("Enter the amount you want to convert:"))
        self.from_country = input("From country: ").upper()
        self.to_country = input("To country: ").upper()
        
        self.api_key = "b2a94afbe7084b65d77830c2"
        self.url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{self.from_country}"

    
    
    def exchange_rate(self):
        data = requests.get(self.url).json()
        
        if(self.to_country in data["conversion_rates"]):
            return data["conversion_rates"][self.to_country]
        else:
            return print("Invalid")
            return none
        
    
    def convert(self):
        rate = self.exchange_rate()
        if rate:
            converted_amount = self.amount * rate
            print(f"{self.amount} {self.from_country} = {converted_amount:.1f} {self.to_country}")
        else:
            print("Conversion failed.")

converter = Currency_converter()
converter.convert()

            
    
    
    
