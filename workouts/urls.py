from django.urls import path
from .views import *

urlpatterns = [
    path('workouts', WorkoutListView.as_view(), name='workouts'),
    path('add-workout', WorkoutCreateView.as_view(), name="add-workout")
]