from django.shortcuts import render
from rest_framework import viewsets

from .serializers import InterviewSerializer
from .models import Interview, Photograph
# Create your views here.

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
