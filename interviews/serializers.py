from rest_framework import serializers

from .models import Interview, Photograph

class InterviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interview
        fields = ('full_name', 'date', 'text')
