from django.shortcuts import render, get_object_or_404
from .models import Workout


# Views.
def workout(request, workout_id):
    """
    View Workout and render same to user.
    :param request:
    :param workout_id:
    :return:
    """
    workout = get_object_or_404(Workout, pk=workout_id)

    context = {
        'workout': workout
    }

    return render(request, 'workouts/workout-view.html', context)
