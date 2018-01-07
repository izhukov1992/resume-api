from rest_framework import serializers

from .models import Education


class EducationsSerializer(serializers.ModelSerializer):
    """Serializer of Education model.
    """

    class Meta:
        model = Education
        exclude = ('user', )
