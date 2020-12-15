from django.test import TestCase
from about.forms import ContactForm

import logging
import logging.config
logger = logging.getLogger('django') #__name__ specifies the module name, django is the general purpose logger


class TestPlanForms(TestCase):


    def test_about_contact_valid_form(self): 

        form = ContactForm(
            {
                "name": "test name", # max_length=100
                "subject": "test subject", # max_length=100
                "email":"testuser@emailaddress.com",
                "message": "Test Message Contents"

            }
        )
        self.assertTrue(form.is_valid())

    def test_about_contact_email_invalid_form(self): 

        form = ContactForm(
            {
                "name": "test name", # max_length=100
                "subject": "test subject", # max_length=100
                "email":"testuser broken emailaddress.com",
                "message": "Test Message Contents"

            }
        )
        self.assertFalse(form.is_valid())

    def test_about_contact_message_length_invalid_form(self): 

        form = ContactForm(
            {
                "name": "test name", # max_length=100
                "subject": "test subject", # max_length=100
                "email":"testuser broken emailaddress.com",
                "message": "Test"

            }
        )
        self.assertFalse(form.is_valid())

    def test_about_contact_blank_name_invalid_form(self): 

        form = ContactForm(
            {
                "name": "", # max_length=100
                "subject": "test subject", # max_length=100
                "email":"testuser broken emailaddress.com",
                "message": "Test"

            }
        )
        self.assertFalse(form.is_valid())