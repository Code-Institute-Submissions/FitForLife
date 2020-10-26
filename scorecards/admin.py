from django.contrib import admin
from .models import Scorecard

# Register your models here.


class ScorecardAdmin(admin.ModelAdmin):
    list_display = (
        'workout_id',
        'plan_id',
        'user_profile_id',
        'repititions',
        'score',
        'week_reference'
    )

    ordering = ('user_profile_id',)


admin.site.register(Scorecard, ScorecardAdmin)