from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework import mixins, viewsets, filters

from posts.models import Post, Group, Follow
from .serializers import (FollowSerializer,
                          GroupSerializer,
                          PostSerializer,
                          CommentSerializer)
from .permissions import IsAutherOrReadOnly


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAutherOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsAutherOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class ListCreateViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    pass


class FollowViewSet(ListCreateViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        follows = Follow.objects.filter(user=user)
        return follows

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
