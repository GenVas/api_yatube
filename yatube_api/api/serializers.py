from django.shortcuts import get_object_or_404
from rest_framework import serializers

from posts.models import Comment, Group, Post, User


class CommentSerializer(serializers.ModelSerializer):

    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')

    def update(self, instance, validated_data):
        comments = validated_data.pop('comments', [])
        instance = super().update(instance, validated_data)
        for comment in comments:
            current_comment = get_object_or_404(Comment, pk=comment.id)
            instance.comments.add(current_comment)
        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('pk', 'title')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    # group = serializers.SlugRelatedField(read_only=True, slug_field='title')
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author', 'pub_date')
