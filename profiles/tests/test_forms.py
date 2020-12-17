from django.test import TestCase
from profiles.forms import UserProfileForm


class TestUserProfileForms(TestCase):

    def test_excluded_profile_fields_in_meta(self):
        """ check if correct fields are in Metaclass """
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ("user","is_member","is_life_member"))

    def test_profile_valid_form(self):
        form = UserProfileForm(
            {
                "default_phone_number": "08688776632",
                "default_street_address1": "Street Address 1",
		"default_street_address2": "Street Address 2",
                "default_town_or_city": "Limerick",
                "default_postcode": "VA25678",
                "default_country": "US",
		"default_county" : "Limerick",
                "is_member": False,    
                "is_life_member": False, 
            }
        )
        self.assertTrue(form.is_valid())
