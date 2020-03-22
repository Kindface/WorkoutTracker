from django.contrib import admin
from .models import Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['date', 'owner', 'description']

admin.site.register(Workout, WorkoutAdmin)
