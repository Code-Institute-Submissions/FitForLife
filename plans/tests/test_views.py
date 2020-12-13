from django.test import TestCase
from plans.models import Plan
from django.contrib.auth import get_user_model


class TestPlanViews(TestCase):
    def setUp(self):

        """ Tests for Plan Views """
        #print("Running setup code in Plan Views Testing")
        user_model = get_user_model()
        user_model.objects.create_user(
            "testuser", "testuser@gmail.com", "testuser"
        )
        temp_plan = Plan.objects.create(
            plan_name="test_plan", description="test_description",
            details="testdetail1,testdetail2,testdetail3"
        )
        

    def test_get_all_plans_page(self):
        """ get Plan page response good """
        # filter by All
        response = self.client.get(
            "/plans/?sort=plan_name&direction=asc")
        #print("Response is " + str(response))
        context = response.context.get('current_sorting')
        #print("Context is " + str(context))
        self.assertEqual(response.status_code, 200)
        # filter by category
        response = self.client.get(
            "/plans/?sort=plan_name&direction=asc")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(context, "plan_name_asc")
        # filter by query
        response = self.client.get("/plans/?q=weight")
        self.assertEqual(response.status_code, 200)
        # filter by query no input
        response = self.client.get("/plans/?q", follow=True)
        message = list(response.context.get("messages"))[0]
        # no search term provided
        self.assertEqual(message.tags, "error")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "plans/plans.html")

    # return 404 if url incorrect
    def test_get_all_plans_404(self):
        response = self.client.get("/plans/doesnotexist")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    # get Plan details page response good
    def test_get_Plan_detail_page(self):
        temp_plan = Plan.objects.create(
            plan_name="test_plan", description="test_description",
            details="testdetail1,testdetail2,testdetail3"
        )
        #print("Plan id is " + f"/plans/{temp_plan.id}/")
        response = self.client.get(f"/plans/{temp_plan.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "plans/plan_detail.html")





