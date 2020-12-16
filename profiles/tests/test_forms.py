from django.test import TestCase
from profiles.forms import UserProfileForm


class TestUserProfileForms(TestCase):
    def test_profile_fields_in_meta(self):
        """ check if correct fields are in Metaclass """
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ("user","is_member","is_life_member"))

    def test_profile_valid_form(self):
        form = UserProfileForm(
            {
                "default_phone_number": "123245",
                "default_street_address1": "23 tehioadf",
                "default_town_or_city": "hometown",
                "default_postcode": "123jdf",
                "default_country": "US",
                "is_member": False,    
                "is_life_member": False, 
            }
        )
        self.assertTrue(form.is_valid())
