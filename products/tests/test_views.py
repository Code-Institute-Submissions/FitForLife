from django.test import TestCase
from products.models import Product, Category
from django.contrib.auth import get_user_model


class TestProductViews(TestCase):
    def setUp(self):

        """ Tests for Product Views """
        #print("Running setup code in Product Views Testing")
        category = Category.objects.create(name="test_category",friendly_name="Test Category")
        user_model = get_user_model()
        user_model.objects.create_user(
            "testuser", "testuser@gmail.com", "testuser"
        )
        temp_product = Product.objects.create(
            product_name="test_product", description="test_description",price=0,
            product_part_number="1122334455", category=category
        )
        

    def test_get_all_products_page(self):
        """ get Product page response good """
        # filter by All
        response = self.client.get(
            "/products/?category=test_category&sort=price&direction=asc")
        #print("Response is " + str(response))
        context = response.context.get('current_sorting')
        #print("Context is " + str(context))
        self.assertEqual(response.status_code, 200)
        # filter by category
        response = self.client.get(
            "/products/?category=test_category&sort=price&direction=asc")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(context, "price_asc")
        # filter by query
        response = self.client.get("/products/?q=car")
        self.assertEqual(response.status_code, 200)
        # filter by query no input
        response = self.client.get("/products/?q", follow=True)
        message = list(response.context.get("messages"))[0]
        # no search term provided
        self.assertEqual(message.tags, "error")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    # return 404 if url incorrect
    def test_get_all_products_404(self):
        response = self.client.get("/products/doesnotexist")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    # get Product details page response good
    def test_get_Product_detail_page(self):
        category = Category.objects.create(name="test_category",friendly_name="Test Category")
        temp_product = Product.objects.create(
            product_name="test_product", description="test_description",price=0,
            product_part_number="1122334455", category=category
        )
        #print("Product id is " + f"/products/{temp_product.id}/")
        response = self.client.get(f"/products/{temp_product.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")





