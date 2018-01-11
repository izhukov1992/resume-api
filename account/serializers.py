from django.conf import settings
from rest_framework import serializers

from socials.serializers import SocialsSerializer
from jobs.serializers import JobsSerializer
from educations.serializers import EducationsSerializer
from skills.serializers import SkillsSerializer

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    """Serializer of Account model.
    """

    userpic = serializers.SerializerMethodField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    socials = SocialsSerializer(source='user.social_set', many=True)
    jobs = JobsSerializer(source='user.job_set', many=True)
    educations = EducationsSerializer(source='user.education_set', many=True)
    skills = SkillsSerializer(source='user.skill_set', many=True)

    def get_userpic(self, obj):
        return '%s%s' % (settings.MEDIA_URL, obj.userpic)

    class Meta:
        model = Account
        exclude = ('user', )
