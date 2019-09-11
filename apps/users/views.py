from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from social_django.models import UserSocialAuth
from json import dumps

from .models import UserProfile
from .serializers import UserDetailSerializer


# Create your views here.
class UserDetailViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.avatar:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

        social_user = UserSocialAuth.objects.get(user=instance)

        if social_user:
            extra_data = social_user.extra_data
            profile_image_url = extra_data["profile_image_url"]
            if profile_image_url:
                instance.avatar = profile_image_url
                instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_object(self):
        return self.request.user
