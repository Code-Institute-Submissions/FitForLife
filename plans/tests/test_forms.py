from django.test import TestCase
from plans.forms import PlanForm
from workouts.models import Workout

import logging
import logging.config
logger = logging.getLogger('django') #__name__ specifies the module name, django is the general purpose logger


class TestPlanForms(TestCase):

    def test_plan_valid_form(self):
        workout1 = Workout.objects.create(workout_name="test_workout 1",description="Workout 1")
        workout2 = Workout.objects.create(workout_name="test_workout 2",description="Workout 2")
        workout3 = Workout.objects.create(workout_name="test_workout 3",description="Workout 3")
        logger.warn(str(workout1))
        workouts = [workout1,workout2,workout3]
        form = PlanForm(
            {
                "plan_name": "test plan name",
                "description": "test description",
                "details":"testdetail1,testdetail2,testdetail3",
                "image_url": "http://127.0.0.1:8000/plans/edit/3/",
                "workouts": workouts

            }
        )
        self.assertTrue(form.is_valid())
