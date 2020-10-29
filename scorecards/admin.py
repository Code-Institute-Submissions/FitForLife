from django.contrib import admin
from .models import Scorecard
from .models import Workout

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
    readonly_fields = ('current_week_number',)

    ordering = ('user_profile_id',)

    def current_week_number(self, obj):
        return obj.current_week_number()

        

admin.site.register(Scorecard, ScorecardAdmin)
