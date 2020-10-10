from django.db import models

# we inherit the base model


class PlanCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Plan(models.Model):
    category = models.ForeignKey('PlanCategory', null=True, blank=True, on_delete=models.SET_NULL)
    plan_part_number = models.CharField(max_length=254, null=True, blank=True)
    plan_name = models.CharField(max_length=254,null=True)
    description = models.TextField(null=True)
    details = models.TextField(max_length=254,null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    duration = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.plan_name

    def get_friendly_name(self):
        return self.friendly_name