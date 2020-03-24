from django.urls import path
from .views import *

urlpatterns = [
    path('runs', RunListView.as_view(), name='runs'),
    path('add-run', RunCreateView.as_view(), name="add-run"),
    path('run/<int:pk>/delete/', delete_run, name='delete-run'),
    path('run/<int:pk>/edit/', RunUpdateView.as_view(), name='edit-run')
]
