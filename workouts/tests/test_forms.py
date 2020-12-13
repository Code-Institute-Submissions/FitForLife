from django.test import TestCase
from workouts.forms import WorkoutForm
from workouts.models import Workout
from plans.models import Plan

import logging
import logging.config
logger = logging.getLogger('django') #__name__ specifies the module name, django is the general purpose logger


class TestWorkoutForms(TestCase):

    def test_workout_valid_form(self):
        plan1 = Plan.objects.create(plan_name="test_plan 1",description="Plan 1")
        plan2 = Plan.objects.create(plan_name="test_plan 2",description="Plan 2")
        plan3 = Plan.objects.create(plan_name="test_plan 3",description="Plan 3")

        plans = [plan1,plan2,plan3]
        form = WorkoutForm(
            {
                "workout_name": "test workout name",
                "description": "test description",
                "points": 12,
                "instructions":"testinstructions1,testinstructions2,testinstructions3",
                "image_url": "http://127.0.0.1:8000/workouts/edit/3/",
                "plans": plans

            }
        )
        self.assertTrue(form.is_valid())
