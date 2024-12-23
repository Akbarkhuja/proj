from rest_framework import serializers

from .models import Education, Job
from users.serializers import ApplicantSerializer


class EducationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=ApplicantSerializer(required=True))

    class Meta:
        model = Education
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=ApplicantSerializer)

    class Meta:
        model = Job
        fields = '__all__'