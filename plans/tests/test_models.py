from django.test import TestCase
from plans.models import Plan


class TestPlanModels(TestCase):
    def test_plan_creation_defaults(self):
        """ test the Plan creation """
        temp_plan = Plan.objects.create(
            plan_name="test_plan", description="test_description",
            details="testdetail1,testdetail2,testdetail3"
        )

        self.assertEqual(temp_plan.plan_name, "test_plan")
        self.assertEqual(temp_plan.description, "test_description")
        self.assertEqual(temp_plan.details,"testdetail1,testdetail2,testdetail3")

class TestPlanModel(TestCase):



    def test_plan_string_method_returns_name(self):
        plan = Plan.objects.create(
            plan_name="Test Plan", description="test_description",
            details="testdetail1,testdetail2,testdetail3"
        )
        self.assertEqual(str(plan), 'Test Plan')

    def test_plan_string_method_returns_description(self):
        plan = Plan.objects.create(
            plan_name="test_plan", description="Test Plan description",
            details="testdetail1,testdetail2,testdetail3"
        )
        self.assertEqual(str(plan.description), 'Test Plan description')


    def test_plan_string_method_returns_details(self):
        plan = Plan.objects.create(
            plan_name="test_plan", description="test_description",
            details="testdetail1,testdetail2,testdetail3"
        )
        self.assertEqual(str(plan.details), 'testdetail1,testdetail2,testdetail3')

