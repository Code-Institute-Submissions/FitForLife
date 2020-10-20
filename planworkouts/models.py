from django.db import models
from plans.models import Plan
from workouts.models import Workout



# Create your models here.




class PlanWorkout(models.Model):
    plan_id = models.ForeignKey('plans.Plan', null=True, blank=True, on_delete=models.SET_NULL)
    workout_id = models.ForeignKey('workouts.Workout', null=True, blank=True, on_delete=models.SET_NULL)
    repetitions = models.IntegerField(null=True)






