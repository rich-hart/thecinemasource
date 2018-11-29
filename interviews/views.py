from rest_framework import viewsets, filters

from .models import Post, Photograph
from .serializers import PostSerializer, PhotographSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'title')

class PhotographSerializer(viewsets.ModelViewSet):
    queryset = Photograph.objects.all()
    serializer_class = PhotographSerializer
