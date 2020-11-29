from django.test import TestCase
from products.forms import ProductForm


class TestProductForms(TestCase):

    def test_product_valid_form(self):
        form = ProductForm(
            {
                "product_name": "test name",
                "description": "test description",
                "price": "12",
            }
        )
        self.assertTrue(form.is_valid())
