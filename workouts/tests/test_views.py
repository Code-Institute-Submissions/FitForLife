from django.test import TestCase
from workouts.models import Workout
from django.contrib.auth import get_user_model


class TestWorkoutViews(TestCase):
    def setUp(self):

        """ Tests for Workout Views """
        #print("Running setup code in Workout Views Testing")
        user_model = get_user_model()
        user_model.objects.create_user(
            "testuser", "testuser@gmail.com", "testuser"
        )
        temp_workout = Workout.objects.create(
            workout_name="test_workout", description="test_description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )
        

    def test_get_all_workouts_page(self):
        """ get Workout page response good """
        # filter by All
        response = self.client.get(
            "/workouts/?sort=workout_name&direction=asc")
        #print("Response is " + str(response))
        context = response.context.get('current_sorting')
        #print("Context is " + str(context))
        self.assertEqual(response.status_code, 200)
        # filter by category
        response = self.client.get(
            "/workouts/?sort=workout_name&direction=asc")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(context, "workout_name_asc")
        # filter by query
        response = self.client.get("/workouts/?q=bend")
        self.assertEqual(response.status_code, 200)
        # filter by query no input
        response = self.client.get("/workouts/?q", follow=True)
        message = list(response.context.get("messages"))[0]
        # no search term provided
        self.assertEqual(message.tags, "error")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workouts/workouts.html")

    # return 404 if url incorrect
    def test_get_all_workouts_404(self):
        response = self.client.get("/workouts/doesnotexist")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    # get Workout instructions page response good
    def test_get_Workout_detail_page(self):
        temp_workout = Workout.objects.create(
            workout_name="test_workout", description="test_description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )
        #print("Workout id is " + f"/workouts/{temp_workout.id}/")
        response = self.client.get(f"/workouts/{temp_workout.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workouts/workout_detail.html")





