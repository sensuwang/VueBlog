__author__ = 'sensuu'
__date__ = '2019/5/27 19:02'
from rest_framework import serializers

from .models import Reply, Comment
from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "username")


class UserPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "username", "avatar")


class ReplySerializer(serializers.ModelSerializer):
    user_info = UserSerializer()

    class Meta:
        model = Reply
        fields = ("id", "created", "content", "user_info")


class ReplyCreatedSerializer(serializers.ModelSerializer):
    user_info = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Reply
        fields = ("id", "user_info", "content", "comment")


class CommentSerializer(serializers.ModelSerializer):
    replys = ReplySerializer(many=True)
    user_id = UserPicSerializer()

    class Meta:
        model = Comment
        fields = ("id", "aid", "content", "user_id", "updated", "created", "replys")


class CommentCreatedSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ("id", "user_id", "aid", "content")
