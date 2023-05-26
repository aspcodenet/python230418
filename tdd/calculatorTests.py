# TEST DRIVEN DEVELOPMENT
import unittest
from calculator import *

# can I buy beer?
# om promilleHalten > 1.0 INTE 
# om över 20 och på systemet -> öl
# om över 18 och på krogen  -> öl
class CalculatorTests(unittest.TestCase):
    def test_when_promillehalt_is_too_high_not_allowed(self):
        # ARRANGE
        promilleHalt = 1.2
        # ACT
        result = canIBuyBeer(30,"Krogen", promilleHalt)
        # ASSSERT      
        self.assertFalse(result)  

    def test_when_psystemet_and_over_20_and_too_drunk_not_allowed(self):
        # ARRANGE
        age = 21
        promilleHalt = 1.5
        # ACT
        result = canIBuyBeer(age,"Systemet", 1.5)
        # ASSSERT      
        self.assertEquals(False, result)
        #self.assertTrue(result)  


    def test_when_psystemet_and_over_20_allowed(self):
        # ARRANGE
        age = 21
        # ACT
        result = canIBuyBeer(age,"Systemet", 0)
        # ASSSERT      
        self.assertEquals(True, result)
        #self.assertTrue(result)  


    def test_when_krogen_and_over_18_allowed(self):
        # ARRANGE
        age = 18
        # ACT
        result = canIBuyBeer(age,"Krogen", 0)
        # ASSSERT      
        self.assertEquals(True, result)
        #self.assertTrue(result)  



unittest.main()