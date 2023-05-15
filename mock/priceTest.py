from price import calculatePrice
import unittest

class priceCalculationtests(unittest.TestCase):
    def test_when_not_pensionar_no_discount(self):
        price = 100
        isPensionar = False

        result = calculatePrice(price,isPensionar)

        self.assertEqual(100, result)

unittest.main()       


