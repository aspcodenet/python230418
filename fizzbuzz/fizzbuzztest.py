import unittest
from fizzbuzz import GetFizzBuzz

class FizzbuzzTest(unittest.TestCase):
    def test_when_divisable_by_3_should_return_fizz(self):
        #arrange
        tal = 12
        # act
        result = GetFizzBuzz(tal)
        # assert            
        self.assertEqual("Fizz",result)
    
    def test_when_divisable_by_5_should_return_buzz(self):
        #arrange
        tal = 10
        # act
        result = GetFizzBuzz(tal)
        # assert            
        self.assertEqual("Buzz",result)

    def test_when_divisable_by_3_and_5_should_return_buzz(self):
        #arrange
        tal = 15
        # act
        result = GetFizzBuzz(tal)
        # assert            
        self.assertEqual("FizzBuzz",result)

    def test_when_not_divisable_by_3_or_5_should_return_number_as_string(self):
        #arrange
        tal = 19
        # act
        result = GetFizzBuzz(tal)
        # assert            
        self.assertEqual("19",result)


unittest.main()


