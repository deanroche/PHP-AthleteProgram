from django.urls import path
from . import views


urlpatterns = [
    path('workout-view', views.workout, name='workout-view')
]
