from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Models
class Workout(models.Model):
    """
    Model to define the fields required to create workouts per day.
    """
    title = models.CharField(max_length=150)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    part_a = models.TextField()
    part_b = models.TextField()
    part_c = models.TextField()
    coach_comments = models.TextField()

    def __str__(self):
        return self.title
