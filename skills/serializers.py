from rest_framework import serializers

from .models import Skill


class SkillsSerializer(serializers.ModelSerializer):
    """Serializer of Skill model.
    """

    class Meta:
        model = Skill
        exclude = ('user', )
