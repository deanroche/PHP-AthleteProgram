from django.db import models
from django.contrib.auth.models import User

# Categories
categories = [
    ('', 'Select Workout Category'),
    ('crossfit', 'Crossfit'),
    ('gymnastics', 'Gymnastics'),
    ('metcon', 'Metcon'),
    ('olympic weightlifting', 'Olympic Weightlifting'),
    ('strength and conditioning', 'Strength & Conditioning'),
]


def get_coach():
    return User.objects.get(id=1)


print(get_coach)


# Models
class Workout(models.Model):
    """
    Model to define the fields required to create workouts per day.
    """
    title = models.CharField(max_length=150)
    coach = models.ForeignKey(User, default=get_coach, on_delete=models.CASCADE)
    workout_date = models.DateField()
    category = models.CharField(max_length=25, choices=categories)
    part_a = models.TextField()
    part_b = models.TextField()
    part_c = models.TextField()
    coach_comments = models.TextField()

    def __str__(self):
        return self.title
