from django.shortcuts import render


# Create your views here.
def workout(request):
    return render(request, 'workouts/workout-view.html')
