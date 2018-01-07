from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    """Model of users' jobs.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    hire = models.DateField()
    fire = models.DateField(null=True, blank=True)
