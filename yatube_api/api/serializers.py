from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Follow, Group
from posts.models import User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created',)
        model = Comment

    def validate(self, data):
        post_id = self.context['request'].parser_context['kwargs']['post_id']

        if not Post.objects.filter(pk=post_id).exists():
            raise serializers.ValidationError(
                'Поста, для которого вы пытаетесь '
                'сделать комментарий, несуществует!')
        return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        slug_field='username')
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    def validate(self, data):
        if data['following'] == self.context.get('request').user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самго себя!')
        return data

    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following')
        )
    ]

    class Meta:
        model = Follow
        fields = ('user', 'following',)
