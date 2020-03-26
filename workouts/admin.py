from django.contrib import admin
from .models import Workout, Exercise


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['date', 'owner', 'description']


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'sets', 'reps']


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise, ExerciseAdmin)