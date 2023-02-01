from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username']


class PostSerializer(serializers.ModelSerializer):
    # username = serializers.ReadOnlyField(source='author.username')
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ['pk', 'content', 'created_at', 'updated_at', 'author']
