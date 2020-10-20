from django.contrib import admin
from .models import PlanWorkout

# Register your models here.


class PlanWorkoutAdmin(admin.ModelAdmin):
    list_display = (
        'plan_id',
        'workout_id',
        'repetitions',
    )


admin.site.register(PlanWorkout, PlanWorkoutAdmin)