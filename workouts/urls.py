from django.urls import path
from .views import *

urlpatterns = [
    path('workouts', WorkoutListView.as_view(), name='workouts'),
    path('add-workout', WorkoutCreateView.as_view(), name="add-workout"),
    path('workout/<int:pk>/', WorkoutDetailView.as_view(), name="workout_detail"),
    path('workout/<int:pk>/delete/', delete_workout, name='delete-workout'),
    path('workout/<int:pk>/edit/', workout_edit, name='edit-workout')
]