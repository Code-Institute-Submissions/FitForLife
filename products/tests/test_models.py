from django.test import TestCase
from products.models import Product, Category


class TestProductModels(TestCase):
    def test_Product_creation_defaults(self):
        """ test the Product creation """
        category = Category.objects.create(name="test_category",friendly_name="Test Category")
        temp_product = Product.objects.create(
            product_name="test_product", description="test_description",price=0,
            product_part_number="1122334455", category=category
        )
        self.assertEqual(temp_product.price, 0)
        self.assertEqual(temp_product.product_name, "test_product")
        self.assertEqual(temp_product.description, "test_description")
        self.assertEqual(temp_product.product_part_number,"1122334455")
        self.assertEqual(temp_product.category,category)

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

    def test_category_string_method(self):
        """ test the category strings """
        temp_category = Category.objects.create(
            name="test_category", friendly_name="test category",
        )
        self.assertEqual(str(temp_category), "test_category")
        self.assertEqual(str(
            temp_category.get_friendly_name()), "test category")