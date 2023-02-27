from rest_framework import serializers
from django.contrib.auth import get_user_model

from posts.models import Post, Group, Comment, Follow


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post', )
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True,
                                        slug_field='username')
    following = serializers.SlugRelatedField(queryset=User.objects.all(),
                                             slug_field='username')

    class Meta:
        fields = ('user', 'following')
        model = Follow
