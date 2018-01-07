from django.db import models
from django.contrib.auth.models import User

from .constants import SKILLS


class Skill(models.Model):
    """Model of users' skills.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=SKILLS)
