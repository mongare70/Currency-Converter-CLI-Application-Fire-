import requests
import fire

# currency convert class
class CurrencyConverter:

    # constructor
    def __init__(self, base_currency, result_currency, amount_to_convert):
        self.base = base_currency
        self.result = result_currency
        self.amount = amount_to_convert


    # Convert currency method
    def convert(self):
        
        url = "https://currency-converter5.p.rapidapi.com/currency/convert"

        querystring = {"format":"json","from":self.base,"to":self.result,"amount":"{}".format(self.amount)}

        headers = {
            'x-rapidapi-key': "4c7fdf69eemsh8d6039574576e92p17fed4jsnf84661b04230",
            'x-rapidapi-host': "currency-converter5.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return response.text

if __name__ == "__main__":
    fire.Fire(CurrencyConverter)