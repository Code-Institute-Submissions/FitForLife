from django.test import TestCase
from planworkouts.models import PlanWorkout
from workouts.models import Workout
from plans.models import Plan
from django.contrib.auth import get_user_model


class TestPlanWorkoutViews(TestCase):
    def setUp(self):

        """ Tests for PlanWorkout Views """
        #print("Running setup code in PlanWorkout Views Testing")
        user_model = get_user_model()
        user_model.objects.create_user(
            "testuser", "testuser@gmail.com", "testuser"
        )
        testplan1 = Plan.objects.create(
            plan_name="Test Plan", description="test_description",
            details="testdetail1,testdetail2,testdetail3"
        )
        testworkout1 = Workout.objects.create(
            workout_name="Test Workout", description="test_description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )
        temp_planworkout = PlanWorkout.objects.create(
            plan_id=testplan1, workout_id=testworkout1,
            
        )
        

    def test_get_all_planworkouts_page(self):
        """ get PlanWorkout page response good """
        # filter by All
        response = self.client.get(
            "/planworkouts/?sort=plan_id&direction=asc")
        #print("Response is " + str(response))
        context = response.context.get('current_sorting')
        #print("Context is " + str(context))
        self.assertEqual(response.status_code, 200)
        # filter by category
        response = self.client.get(
            "/planworkouts/?sort=plan_id&direction=asc")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(context, "plan_id_asc")
        # filter by query
        response = self.client.get("/planworkouts/?q=1")
        self.assertEqual(response.status_code, 200)
        # filter by query no input
        response = self.client.get("/planworkouts/?q", follow=True)
        message = list(response.context.get("messages"))[0]
        # no search term provided
        self.assertEqual(message.tags, "error")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "planworkouts/planworkouts.html")

    # return 404 if url incorrect
    def test_get_all_planworkouts_404(self):
        response = self.client.get("/planworkouts/doesnotexist")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    # get PlanWorkout repititions page response good
    def test_get_planworkout_detail_page(self):
        testplan1 = Plan.objects.create(
            plan_name="Test Plan", description="test_description",
            details="testdetail1,testdetail2,testdetail3"
        )
        testworkout1 = Workout.objects.create(
            workout_name="Test Workout", description="test_description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )
        temp_planworkout = PlanWorkout.objects.create(
            plan_id=testplan1, workout_id=testworkout1,    
        )
        #print("PlanWorkout id is " + f"/planworkouts/{temp_planworkout.id}/")
        response = self.client.get(f"/planworkouts/{temp_planworkout.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "planworkouts/planworkout_detail.html")





