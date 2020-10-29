from django.db import models
from plans.models import Plan
from workouts.models import Workout
from workouts.models import Workout
from profiles.models import UserProfile
from django.utils.timezone import now, datetime
import logging
import logging.config

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
    user_profile_id = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,null=True, blank=True,related_name='scorecards')
    repititions = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    score = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    week_reference = models.DecimalField(max_digits=6, decimal_places=2,null=True)

 

    def __str__(self):
        return str(self.user_profile_id) + "_scorecard"

    def current_week_number(self):
        #today = datetime.datetime.now()
        logger = logging.getLogger('django') #__name__ specifies the module name, django is the general purpose logger
        logger.warn('now = ' + str(0))
        week_number = datetime.date(now()).isocalendar()[1]
        logger.warn('week number = ' + str(week_number) + " " + str(now()) )
        return str(week_number) #[1]   #return the associated week number

    def create_new_scorecard(self):
        # Create a model Store instance
        scorecard = Scorecard(workout_id='1',plan_id='1',user_profile_id='1',repitions='10',score='0',week_reference='1')
        scorecard.save()


