from django.test import TestCase
from .models import Product
# Create your tests here.


class TestProductModel(TestCase):

    def test_product_model(self): 
        product = Product.object.Create(product_name="Test Product")
        self.assertEquals("Test Product")
