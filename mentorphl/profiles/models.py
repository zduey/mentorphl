from datetime import timedelta

from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Base model for all profile types """
    MENTOR = "MENTOR"
    MENTEE = "MENTEE"
    ORGANIZATION = "ORGANIZATION"
    PROFILE_CHOICES = (
        (MENTOR, "Mentor"),
        (MENTEE, "Mentee"),
        (ORGANIZATION, "Organization")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=64, choices=PROFILE_CHOICES)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    thumbnail = models.ImageField(upload_to='thumbnails')
    complete = models.BooleanField(default=False, editable=False)

    def is_live(self):
        """ Check if profile is complete """
        return self.complete

    def make_live(self):
        """ Toggle member variable to indicator profile is complete and ready to use """
        self.complete = True
        return

    def get_absolute_url(self):
        return reverse('profiles:view', kwargs={'pk': self.pk})


    def __str__(self):
        return ":".join([self.user, self.user_type, self.name])


class Mentor(Profile):
    """ Mentor profile model """
    SPIRITUAL = "SPIRITUAL"
    PEER = "PEER"
    COMMUNICATION = "COMMUNICATION"
    EDUCATION = "EDUCATION"
    PROFESSIONAL = "PROFESSIONAL"

    SPECIALTY_CHOICES = (
        (SPIRITUAL, "Spiritual"),
        (PEER, "Peer"),
        (COMMUNICATION, "Communication"),
        (EDUCATION, "Education"),
        (PROFESSIONAL, "Professional")
    )
    specialty = models.CharField(max_length=64, choices=SPECIALTY_CHOICES)

    def __str__(self):
        return ":".join([self.name, self.specialty])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Mentor.objects.create(user=instance)
    return

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    return


class Mentee(Profile):
    """ Model for storing informaton about mentees """
    # one-to-many relationship with mentors (1::5 roughly?)
    def __str__(self):
        return super().__str__()


class Organization(Profile):
    """ Profile model for organizations taking part in MentorPhilly """
    def __str__(self):
        return super().__str__()
