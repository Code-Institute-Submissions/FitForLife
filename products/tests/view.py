from django.test import SimpleTestCase
from .models import Product
# Create your tests here.


class TestProductView(SimpleTestCase):

    def test_get_products(self): 
        response = self.response.get('\')
        self.assertEqual(response.status_code,200)

        
