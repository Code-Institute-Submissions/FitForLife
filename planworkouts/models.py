from django.db import models
#from plans.models import Plan
#from workouts.models import Workout



# Each Plan has a number of associated workouts. The PlanWorkout objects accosiates 
# workouts with a specific plan.
# A row in this table represents the following
# The plan id
# the workout id
# the number of repitions





class PlanWorkout(models.Model):
    plan_id = models.ForeignKey('plans.Plan', null=True, blank=True, on_delete=models.SET_NULL)
    workout_id = models.ForeignKey('workouts.Workout', null=True, blank=True, on_delete=models.SET_NULL)
    repetitions = models.IntegerField(null=True)







