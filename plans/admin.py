from django.contrib import admin
from .models import Plan, PlanCategory

# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'plan_part_number',
        'plan_name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('plan_part_number',)


class PlanCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Plan, PlanAdmin)
admin.site.register(PlanCategory, PlanCategoryAdmin)
