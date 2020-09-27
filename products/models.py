from django.db import models

# we inherit the base model
class Product(models.Model): 
    product_name = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name
    