from django.db import models

# Create your models here.


class About(models.Model):
    contact_email = models.CharField(max_length=254,null=True)

