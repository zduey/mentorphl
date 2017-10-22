from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User


class Mentor(models.Model):
    """ Model for storing information about mentors """
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    thumbnail = models.ImageField(upload_to='thumbnails')


    def __str__(self):
        return self.name

class Mentee(models.Model):
    """ Model for storing informaton about mentees """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumbnails')
