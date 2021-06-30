import unittest
from currency_converter import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):
    
    # test with no command 
    def test_convert_no_command(self):
        self.assertIs(CurrencyConverter().convert(), '92.6042')

    # test with single command 
    def test_convert_single_command(self):
        self.assertEqual(CurrencyConverter("KES").convert(), '92.6042')

    # test with two commands
    def test_convert_two_command(self):
        self.assertEqual(CurrencyConverter("KES", "USD").convert(), '92.6042')

    # test with all commands
    def test_convert_all_command(self):
        self.assertEqual(CurrencyConverter("KES", "USD", 10000).convert(), '92.6042')

    # test with wrong base currency
    def test_convert_wrong_base_currency(self):
        self.assertEqual(CurrencyConverter("HHH", "USD", 10000).convert(), '92.6042')

    # test with wrong result currency
    def test_convert_wrong_result_currency(self):
        self.assertEqual(CurrencyConverter("KES", "HHH", 10000).convert(), '92.6042')

    # test with wrong amount to convert
    def test_convert_wrong_amount_to_convert(self):
        self.assertEqual(CurrencyConverter("KES", "USD", 'HHH').convert(), '92.6042')

    # test with wrong base currency & result currency
    def test_convert_wrong_base_currency_and_result_currency(self):
        self.assertEqual(CurrencyConverter("HHH", "HHH", 10000).convert(), '92.6042')

    # test with wrong base currency & amount_to_convert
    def test_convert_wrong_base_currency_and_amount_to_convert(self):
        self.assertEqual(CurrencyConverter("HHH", "USD", 'HHH').convert(), '92.6042')

    # test with wrong base currency & result currency
    def test_convert_wrong_result_currency_and_amount_to_convert(self):
        self.assertEqual(CurrencyConverter("KES", "HHH", 'HHH').convert(), '92.6042')

    # test with all wrong inputs
    def test_convert_wrong_all(self):
        self.assertEqual(CurrencyConverter("HHH", "HHH", 'HHH').convert(), '92.6042')
    

# if __name__ == '__main__':
#     unittest.main()