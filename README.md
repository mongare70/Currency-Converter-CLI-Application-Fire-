# Currency Converter (CLI Application)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c6f68237fd4b44c29cca3b1e7cd3d5ae)](https://app.codacy.com/gh/mongare70/Currency-Converter-CLI-Application-Fire-?utm_source=github.com&utm_medium=referral&utm_content=mongare70/Currency-Converter-CLI-Application-Fire-&utm_campaign=Badge_Grade_Settings)

>A project done in fulfillment of the first checkpoint of the SkaeHub Developer Program

#1 Problem definition
The main objective of this project is to model a Currency Converter application. 
It converts the amount the user has entered from the base currency to the result currency.
It then prints out a JSON containing the converted currency.

This application uses Rapid API's Currency Converter API 
to convert the currency using the latest currency rates.
  
### The supported currencies for this application are:
* Kenyan Shilling (KES)
* U.S. Dollar (USD)
* European Euro (EUR)
* Japanese Yen (JPY)
* British Pound (GBP)
* Swiss Franc (CHF)
* Canadian Dollar (CAD)
* Australian Dollar (AUD)
* New Zealand Dollar (NZD)
* South African Rand (ZAR)

#2. Installation and setup

1. First clone this repository to your local machine using `https://github.com/mongare70/Currency-Converter-CLI-Application-Fire-`

2. Checkout into the **master** branch using `git checkout master`

3. Create a **virtualenv** on your machine and install the dependencies via `pip install -r requirements.txt` and activate it.

4. cd into the **app** folder and run `python currency_converter.py <command> --base <base_currency> --result <result_currency> --amount <amount_to_convert>`

#3. Usage
The following screencast shows how to run the app. Check it out:



#4. Tests

To run nosetests ensure that you are within the *virtual environment* and have the following installed:

1. *pytest*
2. *pytest-cov*

After ensuring the above, within the **app folder** run :

`pytest` or

`pytest --cov=test_currency_converter`

## Credits

1. [Humphrey Musonye](https://github.com/hmusonye)

2. The [SkaeHub](https://skaehub.com/) community.

