from django.test import TestCase
from django.contrib.auth import get_user_model


class TestAboutViews(TestCase):
       

    def test_get_all_abouts_page(self):
        """ get About page response good """
        # filter by All
        response = self.client.get(
            "/about/")
        #print("Response is " + str(response))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/about.html")

    # return 404 if url incorrect
    def test_get_all_abouts_404(self):
        response = self.client.get("/about/doesnotexist")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")






