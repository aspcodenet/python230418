# integration ofta så är det automatiserade  WEB-anrop 
# https://fakestoreapi.com/products

# Verfiera att andra system fortfarande funkar!
# att vi kan utbyta data så som vi kunnat
# = fånga ändringar som andra gör i sina system
#  ex byte av URL
# FÖREKOMMA kunden
# 

import unittest 
from unittest.mock import Mock,patch
import urllib, json

class ProductTest(unittest.TestCase):
    def test_can_fetch_products(self):
      url = "https://fakestoreapi.com/products"
      response = urllib.urlopen(url)
      data = json.loads(response.read())        
