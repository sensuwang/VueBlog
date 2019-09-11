__author__ = 'sensuu'
__date__ = '2019/5/25 10:43'
from rest_framework import serializers

from .models import UserProfile


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("username", "avatar", )
