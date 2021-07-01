import requests
import fire
import json

# set consisting supported currencies
supported_currencies = {'KES', 'USD', 'EUR', 'JPY', 'GBP', 'CHF', 'CAD', 'AUD', 'ZAR', 'NZD'}

# currency convert class
class CurrencyConverter:
    # constructor
    def __init__(self, base, result, amount):
        self.base = base
        self.result = result
        self.amount = amount

    # Convert currency method
    def convert(self):
        
        # check if base, result, and amount have been parsed
        if self.base and self.result and self.amount:

            # check if base currency and result currency are supported by the CLI app
            if self.base in supported_currencies and self.result in supported_currencies:

                # check if amount is integer or float
                if isinstance(self.amount, int) or isinstance(self.amount, float):
                    url = "https://currency-converter5.p.rapidapi.com/currency/convert"

                    querystring = {"format":"json","from":self.base,"to":self.result,"amount":"{}".format(self.amount)}

                    headers = {
                        'x-rapidapi-key': "4c7fdf69eemsh8d6039574576e92p17fed4jsnf84661b04230",
                        'x-rapidapi-host': "currency-converter5.p.rapidapi.com"
                    }

                    response = requests.request("GET", url, headers=headers, params=querystring)

                    response = response.text

                    # convert currency and put it into a dictionary
                    response = json.loads(response)

                    # return response
                    return response['rates']
                
                else:
                    return False

            else:
                return False
        else:
            return False
        
       

if __name__ == "__main__":
    fire.Fire(CurrencyConverter)