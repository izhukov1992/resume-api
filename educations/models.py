from django.db import models
from django.contrib.auth.models import User


class Education(models.Model):
    """Model of users' educations
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
