from django.urls import path
from . import views

urlpatterns = [
    path('',views.check_auth, name='tracker')
]