from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import UserProfile
from checkout.models import Order
import logging
import logging.config
logger = logging.getLogger('django') #__name__ specifies the module name, django is the general purpose logger

class TestProfileViews(TestCase):
    """ Tests for Profile Views """

    def setUp(self):
        """ Create a secret user """
        user_model = get_user_model()
        user_model.objects.create_user(
            "Jade", "jade@gmail.com", "secret"
        )

    def test_get_user_profile_page(self):
        """ get user profile page as logged in user """
        self.client.login(username="Jade", password="secret")
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_get_user_profile_404(self):
        """ return 404 if url incorrect """
        response = self.client.get("/profile/fewt")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_unregistered_attempt_to_get_profile(self):
        """ redirect from profile if user not logged in """
        response = self.client.get("/profile/", follow=True)
        self.assertRedirects(response, "/accounts/login/?next=%2Fprofile%2F")
        self.assertTemplateUsed(response, "account/login.html")

    def test_update_user_profile(self):
        """ updates the userprofile """
        self.client.login(username="Jade", password="secret")
        data = {"default_phone_number": "08689777634"}
        response = self.client.post("/profile/", data, follow=True)
        self.assertEqual(response.status_code, 200)
        # successful update
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("Profile updated successfully" in message.message)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_invalid_update_user_profile(self):
        """ invalid updates the userprofile """
        self.client.login(username="Jade", password="secret")
        data = {
            "default_phone_number": "08689777634444444535839045890"
        }
        response = self.client.post("/profile/", data, follow=True)
        self.assertEqual(response.status_code, 200)
        # invalid form update
        message = list(response.context.get("messages"))[0]
        # logger.warn("Form Log Message:[" + str(message)+ "]")
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            "Update failed. Please ensure the form is valid."
            in message.message
        )
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_order_history_view(self):
        """ creates an order and checks it can be accesed in the history """
        self.client.login(username="Jade", password="secret")
        temp_profile = UserProfile.objects.get(user__username="Jade")
        temp_order = Order.objects.create(
            full_name="Jade Sullivan",
            user_profile=temp_profile,
            email="jade@gmail.com",
            phone_number="08689777634",
            country="UK",
            postcode="NY6552",
            town_or_city="Cork City",
            street_address1="Street Name One",
            street_address2="Street Name Two",
            county="yes",
            stripe_pid="456678",
            original_cart="2,4,5",
        )

        response = self.client.get(
            f"/profile/order_history/{temp_order.order_number}", follow=True
        )
        self.assertEqual(response.status_code, 200)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "info")
        self.assertTrue(
            f"This is a past confirmation for order number "
            f"{temp_order.order_number}."
            in message.message
        )
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
