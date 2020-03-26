from django.urls import path
from .views import *

urlpatterns = [
    path('exercises', ExerciseListView.as_view(), name='exercises'),
    path('add-exercises', ExerciseCreateView.as_view(), name='add-exercise')
]