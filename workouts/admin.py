from django.contrib import admin
from .models import Workout

# Register your models here.


class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        'workout_name',
        'description',
        'points',
        'image',
    )

    ordering = ('workout_name',)


admin.site.register(Workout, WorkoutAdmin)