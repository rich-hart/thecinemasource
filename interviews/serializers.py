from rest_framework import serializers

from .models import Post, Photograph

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
#            'deprecated_id',
            'category',
#            'name',
            'title',
            'author',
            'date',
            'excerpt',
            'content',
        )

class PhotographSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photograph
        fields = (
            'id',
            'upload',
            'post',
        )
