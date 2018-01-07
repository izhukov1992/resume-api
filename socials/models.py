from django.db import models
from django.contrib.auth.models import User

from .constants import SOCIALS


class Social(models.Model):
    """Model of users' public resources.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=SOCIALS)
    url = models.URLField()
