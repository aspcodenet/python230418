import unittest
from employee import Customer

class CustomerTests(unittest.TestCase):
    def test_when_not_member_and_cost_is_less_than_1000_then_price_is_unchanged(self):
        # arrange
       
        price = 800 
        c = Customer(False,"Stefan")
        # act
        result = c.calculatePrice(price)
        # assert
        self.assertEqual(result,800)
