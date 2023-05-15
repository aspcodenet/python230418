from price import calculatePrice
import unittest 
from unittest.mock import Mock,patch
import datetime

class priceCalculationtests(unittest.TestCase):
    def test_when_not_pensionar_no_discount(self):
        price = 100
        isPensionar = False

        result = calculatePrice(price,isPensionar)

        self.assertEqual(100, result)

    def test_when_pensionar_and_tuesday_discount(self):
        price = 100
        isPensionar = True

        datetime_mock = Mock()
        datetime_mock.now.return_value = datetime.datetime(2023, 5, 16)        
        with patch('datetime.datetime', new=datetime_mock):
            result = calculatePrice(price,isPensionar)

        self.assertEqual(98, result)


    def test_when_not_pensionar_and_tuesday_no_discount(self):
        price = 100
        isPensionar = False

        datetime_mock = Mock()
        datetime_mock.now.return_value = datetime.datetime(2023, 5, 16)        

        with patch('datetime.datetime', new=datetime_mock):
            result = calculatePrice(price,isPensionar)

        self.assertEqual(100, result)



unittest.main()       


