from django.db import models
from django.contrib.auth.models import User

from .constants import SOCIALS


class Social(models.Model):
    """Model of users' public resources.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=SOCIALS)
    url = models.URLField()
