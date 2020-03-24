from django.urls import path
from .views import *

urlpatterns = [
    path('imts', IMTListView.as_view(), name='imts'),
    path('add-imt',ImtCreateView.as_view(), name='add-imt'),
    path('imt/<int:pk>/delete/', delete_imt, name='delete-imt')
]
