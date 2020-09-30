from django.contrib import admin
from .models import Workout


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'workout_date', 'category')
    list_display_links = ('title', 'workout_date')
    search_fields = ('title',)
    list_per_page = 20
    list_filter = ('category',)


# Models
admin.site.register(Workout, WorkoutAdmin)
