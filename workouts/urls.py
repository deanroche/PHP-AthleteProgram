from django.urls import path
from . import views


urlpatterns = [
    path('workout-view/<int:workout_id>', views.workout, name='workout-view')
]
