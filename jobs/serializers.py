from rest_framework import serializers

from .models import Job


class JobsSerializer(serializers.ModelSerializer):
    """Serializer of Job model.
    """

    class Meta:
        model = Job
        exclude = ('user', )
