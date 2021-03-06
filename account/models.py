from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """Model of users' accounts.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userpic = models.ImageField(upload_to='resume')
    resume = models.TextField()
    interests = models.TextField()
