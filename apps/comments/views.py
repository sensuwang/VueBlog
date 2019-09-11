from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from rest_framework.response import Response

from .serializers import CommentSerializer, CommentCreatedSerializer, ReplyCreatedSerializer, ReplySerializer
from .models import Comment, Reply
from utils.custom_json_response import JsonResponse


# Create your views here.
class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication, )

    def get_serializer_class(self):
        if self.action == "list":
            return CommentSerializer
        elif self.action == "create":
            return CommentCreatedSerializer
        return CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        aid = self.request.query_params.get("aid", None)
        if aid:
            queryset = Comment.objects.filter(aid=aid)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        backserializer = CommentSerializer(instance)
        return Response(backserializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data)


class ReplyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Reply.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "list":
            return ReplySerializer
        elif self.action == "create":
            return ReplyCreatedSerializer
        return ReplySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        queryset = Reply.objects.filter(comment=instance.comment)
        backserializer = ReplySerializer(queryset, many=True)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(backserializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
