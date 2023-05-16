import unittest 
from unittest.mock import Mock,patch
from priceCalculate import calculatePrice
import datetime

class PriceCalculatorTests(unittest.TestCase):
    def test_when_tuesday_and_retired_should_get_discount(self):
        #Arrange
        isRetired = True
        datetime_mock = Mock()
        datetime_mock.now.return_value = datetime.datetime(1972, 8, 1)        
        # datetime.datetime.now()
        #act
        with patch('datetime.datetime', new=datetime_mock):
            result = calculatePrice(100,isRetired)
        #assert
        self.assertEqual(98, result)


    def test_when_not_tuesday_and_retired_should_not_get_discount(self):
        #Arrange
        isRetired = True
        datetime_mock = Mock()
        datetime_mock.now.return_value = datetime.datetime(2023, 5, 15)  # måndag       
        # datetime.datetime.now()
        #act
        with patch('datetime.datetime', new=datetime_mock):
            result = calculatePrice(100,isRetired)
        #assert
        self.assertEqual(100, result)

    def test_when_tuesday_and_not_retired_should_not_get_discount(self):
        #Arrange
        isRetired = False
        datetime_mock = Mock()
        datetime_mock.now.return_value = datetime.datetime(2023, 5, 9)  # måndag       
        # datetime.datetime.now()
        #act
        with patch('datetime.datetime', new=datetime_mock):
            result = calculatePrice(100,isRetired)
        #assert
        self.assertEqual(100, result)




unittest.main()