import unittest 
from salary import calculateDiscountedPrice

class SalaryTests(unittest.TestCase):
    def test_when_not_member_and_cost_is_less_than_1000_then_price_is_unchanged(self):
        # arrange
        isMember = False
        price = 800
        # act
        result = calculateDiscountedPrice(price, isMember)
        # assert
        self.assertEqual(result,800)

    def test_when_member_and_cost_is_less_than_1000_then_price_is_correct(self):
        # arrange
        isMember = True
        price = 100
        # act
        result = calculateDiscountedPrice(price, isMember)
        # assert
        self.assertEqual(result,98)

    def test_when_not_member_and_cost_is_more_than_1000_andless_than_5000_then_price_is_correct(self):
        # arrange
        isMember = False
        price = 2000
        # act
        result = calculateDiscountedPrice(price, isMember)
        # assert
        self.assertEqual(result,1900)


unittest.main()

