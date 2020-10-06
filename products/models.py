from django.db import models

# we inherit the base model


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_part_number = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=254,null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name

    def get_friendly_name(self):
        return self.friendly_name