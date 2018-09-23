from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_locations, name='get_locations'),
    path('directions/',  views.display_directions, name = 'display_directions')
]