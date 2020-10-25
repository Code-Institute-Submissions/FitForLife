from django.test import TestCase
from products.models import Product
# Create your tests here.


class TestProductModel(TestCase):



    def test_product_string_method_returns_name(self):
        product = Product.objects.create(product_name='Test product')
        self.assertEqual(str(product), 'Test product')

    def test_product_string_method_returns_description(self):
        product = Product.objects.create(description='Test product description')
        self.assertEqual(str(product.description), 'Test product description')

    def test_product_decimal_method_returns_rating(self):
        product = Product.objects.create(rating=2)
        self.assertEqual(product.rating, 2)

    def test_product_decimal_method_returns_price(self):
        product = Product.objects.create(price=2)
        self.assertEqual(product.price, 2)