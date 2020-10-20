from django.contrib import admin
from .models import Plan

# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'plan_name',
        'image',
    )

    ordering = ('plan_name',)


admin.site.register(Plan, PlanAdmin)
