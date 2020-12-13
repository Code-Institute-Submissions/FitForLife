from django.test import TestCase
from planworkouts.models import PlanWorkout
from workouts.models import Workout
from plans.models import Plan


class TestPlanWorkoutModels(TestCase):
    def test_planworkout_creation_defaults(self):
        """ test the PlanWorkout creation """
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
            repetitions=12
        )

        self.assertEqual(temp_planworkout.plan_id, testplan1)
        self.assertEqual(temp_planworkout.workout_id, testworkout1)
        self.assertEqual(temp_planworkout.repetitions,12)

class TestPlanWorkoutModel(TestCase):



    def test_planworkout_decimal_method_returns_plan_id(self):
        testplan1 = Plan.objects.create(
            plan_name="Test Plan", description="test_description",
            details="testdetail1,testdetail2,testdetail3"
        )
        testworkout1 = Workout.objects.create(
            workout_name="Test Workout", description="test_description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )
        planworkout = PlanWorkout.objects.create(
            plan_id=testplan1, workout_id=testworkout1,
            repetitions=12
        )
        self.assertEqual(planworkout.plan_id,testplan1)

    def test_planworkout_decimal_method_returns_workout_id(self):
        testplan1 = Plan.objects.create(
            plan_name="Test Plan", description="test_description",
            details="testdetail1,testdetail2,testdetail3"
        )
        testworkout1 = Workout.objects.create(
            workout_name="Test Workout", description="test_description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )
        planworkout = PlanWorkout.objects.create(
            plan_id=testplan1, workout_id=testworkout1,
            repetitions=12
        )
        self.assertEqual(planworkout.workout_id, testworkout1 )


    def test_planworkout_decimal_method_returns_repetitions(self):
        testplan1 = Plan.objects.create(
            plan_name="Test Plan", description="test_description",
            details="testdetail1,testdetail2,testdetail3"
        )
        testworkout1 = Workout.objects.create(
            workout_name="Test Workout", description="test_description",
            instructions="testinstructions1,testinstructions2,testinstructions3"
        )
        planworkout = PlanWorkout.objects.create(
            plan_id=testplan1, workout_id=testworkout1,
            repetitions=12
        )
        self.assertEqual(planworkout.repetitions, 12)

