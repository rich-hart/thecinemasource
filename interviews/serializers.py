from rest_framework import serializers

from .models import Post, Photograph

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'deprecated_id',
            'author',
            'date',
            'content',
            'title',
            'category',
            'excerpt',
            'name',
        )

class PhotographSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photograph
        fields = (
            'upload',
            'post',
        )
