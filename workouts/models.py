from django.db import models

# we inherit the base model




class Workout(models.Model):
    workout_name = models.CharField(max_length=254,null=True)
    description = models.TextField(null=True)
    #instructions can be comma seperated to help in formating on the web page
    instructions = models.TextField(max_length=254,null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    #The pints associated with an single session of this workout
    points = models.DecimalField(max_digits=6, decimal_places=2,null=True)

    #allows us split the comma seperated instructions into a list
    def details_list(self):
        return self.details.split(',')

    def __str__(self):
        return self.workout_name

    def get_friendly_name(self):
        return self.friendly_name