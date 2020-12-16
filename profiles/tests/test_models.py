from django.test import TestCase
from profiles.models import UserProfile
from django.contrib.auth import get_user_model


class TestUserProfileModels(TestCase):
    def setUp(self):
        """ Create a Secret user """
        user_model = get_user_model()
        user_model.objects.create_user(
            "Jade", "jade@gmail.com", "Secret"
        )

    def test_user_profile_creation_string(self):
        """ creates a user profile and tests its str is valid """
        self.client.login(username="Jade", password="Secret")
        temp_profile = UserProfile.objects.get(user__username="Jade")
        self.assertEqual(temp_profile.__str__(), "Jade")
