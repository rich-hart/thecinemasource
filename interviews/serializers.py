from rest_framework import serializers

from .models import Post, Photograph, Favorite

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
            'index',
        )

class PhotographSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photograph
        fields = (
            'id',
            'upload',
            'post',
        )

class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favorite
        fields = (
            'id',
            'post',
            'created',
        )
        read_only_fields = ('id', 'created')
