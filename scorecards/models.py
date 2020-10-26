from django.db import models
from plans.models import Plan
from workouts.models import Workout
from workouts.models import Workout
from profiles.models import UserProfile

# Create your models here.

#User ID
#Workout ID
#Plan ID
#Repetitions Completed
#Week Reference
#Score   



class Scorecard(models.Model):
    workout_id = models.ForeignKey('workouts.Workout', null=True, blank=True, on_delete=models.SET_NULL)
    plan_id = models.ForeignKey('plans.Plan', null=True, blank=True, on_delete=models.SET_NULL)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,null=True, blank=True,related_name='orders')
    repititions = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    score = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    week_reference = models.DecimalField(max_digits=6, decimal_places=2,null=True)

 

    def __str__(self):
        return str(self.user_profile) + "_scorecard"



