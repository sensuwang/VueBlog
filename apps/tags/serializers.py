__author__ = 'sensuu'
__date__ = '2019/5/14 16:33'
from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
