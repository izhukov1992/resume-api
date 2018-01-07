from rest_framework import serializers

from .models import Social


class SocialsSerializer(serializers.ModelSerializer):
    """Serializer of Social model.
    """

    class Meta:
        model = Social
        exclude = ('user', )
