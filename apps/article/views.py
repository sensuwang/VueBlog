from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters as drf_filters
from rest_framework import permissions

from .serializers import ArticleSerializer, PreNextSerializer
from .models import Article, ArticleTag
from utils.custom_json_response import JsonResponse


# Create your views here.
# 自定义分页方法 也可以将其配置到setting中作为全局分页方法
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    # 自定义url检索参数名
    page_query_param = 'currentPage'
    max_page_size = 100


class ArticleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ArticleSerializer
    pagination_class = GoodsPagination
    filter_backends = [drf_filters.OrderingFilter]
    ordering_fields = ["publish_time", "visit_count", "created"]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.visit_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)

    def get_queryset(self):
        queryset = Article.objects.all()
        tagid = self.request.query_params.get('tagId', None)
        if tagid != '' and tagid is not None:
            queryset = Article.objects.filter(article__tag__id=tagid)
        return queryset


class PreNextViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = PreNextSerializer
    queryset = Article.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)
