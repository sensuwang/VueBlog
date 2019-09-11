from django.shortcuts import render
from rest_framework import mixins, viewsets

from .models import Tag
from .serializers import TagSerializer
from utils.custom_json_response import JsonResponse
# Create your views here.


class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
