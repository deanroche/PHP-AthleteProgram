from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Models
class Contact(models.Model):
    """Contact Model"""
    contact_title = models.CharField(max_length=150)
    contact_body = models.TextField()
    contact_name = models.ForeignKey(User, null=True,
                                     blank=True, on_delete=models.CASCADE)
    contact_email = models.EmailField()
    contact_date = models.DateTimeField(default=timezone.now)
    read_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.contact_name}, ' \
               f'{self.contact_date.strftime("%d/%m/%Y @ %H:%M")}, Title: ' \
               f'{self.contact_title}'
