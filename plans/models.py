from django.db import models
#from plans.models import PlanWorkout


# we inherit the base model




class Plan(models.Model):
    plan_name = models.CharField(max_length=254,null=True)
    description = models.TextField(null=True)
    #details can be comma seperated to help in formating on the web page
    details = models.TextField(max_length=254,null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    workouts = models.ManyToManyField('workouts.Workout', through='planworkouts.Planworkout',related_name='workouts')

    #allows us split the comma seperated details into a list
    def details_list(self):
        return self.details.split(',')

    def workouts_list(self):
        return self.workouts.all()

    def __str__(self):
        return self.plan_name

    def get_friendly_name(self):
        return self.friendly_name