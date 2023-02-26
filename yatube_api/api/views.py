from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group, Follow
from api.serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
)

from api.permissions import (
    UpdateDestroyPermission, ReadOnlyPermission,
    FollowPermission
)
from api.exceptions import NotUniqueFollowDenied


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (UpdateDestroyPermission, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (UpdateDestroyPermission, )

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (FollowPermission, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def perform_create(self, serializer):
        user_id = self.request.user
        following_id = serializer.validated_data['following']
        follow_exists = Follow.objects.filter(user=user_id,
                                              following=following_id).exists()
        if follow_exists or user_id == following_id:
            raise NotUniqueFollowDenied()
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user_id = self.request.user
        follow = Follow.objects.filter(user=user_id)
        return follow


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (ReadOnlyPermission, )
