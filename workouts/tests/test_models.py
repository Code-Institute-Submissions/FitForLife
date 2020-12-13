from django.test import TestCase
from workouts.models import Workout


class TestWorkoutModels(TestCase):
    def test_workout_creation_defaults(self):
        """ test the Workout creation """
        temp_workout = Workout.objects.create(
            workout_name="test_workout", description="test_description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )

        self.assertEqual(temp_workout.workout_name, "test_workout")
        self.assertEqual(temp_workout.description, "test_description")
        self.assertEqual(temp_workout.instructions,"testinstructions1,testinstructions2,testinstructions3")

class TestWorkoutModel(TestCase):



    def test_workout_string_method_returns_name(self):
        workout = Workout.objects.create(
            workout_name="Test Workout", description="test_description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )
        self.assertEqual(str(workout), 'Test Workout')

    def test_workout_string_method_returns_description(self):
        workout = Workout.objects.create(
            workout_name="test_workout", description="Test Workout description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )
        self.assertEqual(str(workout.description), 'Test Workout description')


    def test_workout_string_method_returns_instructions(self):
        workout = Workout.objects.create(
            workout_name="test_workout", description="test_description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )
        self.assertEqual(str(workout.instructions), 'testinstructions1,testinstructions2,testinstructions3')

