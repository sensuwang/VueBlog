__author__ = 'sensuu'
__date__ = '2019/5/12 13:46'
from rest_framework import serializers

from .models import Article, ArticleImage, ArticleTag


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ("image", )


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    images = ArticleImageSerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"


class ArticleTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title")


class PreNextSerializer(serializers.ModelSerializer):
    next = serializers.SerializerMethodField()
    prev = serializers.SerializerMethodField()

    def get_next(self, obj):
        ordering = self.context['request'].query_params.get('ordering', None)
        tagid = self.context['request'].query_params.get('tagId', None)
        id = obj.id
        if tagid:
            next_article = Article.objects.filter(article__tag_id=tagid, id__gt=id).order_by(ordering).first()
        else:
            next_article = Article.objects.filter(id__gt=id).order_by(ordering).first()
        return ArticleTitleSerializer(next_article, many=False, context={'request': self.context['request']}).data

    def get_prev(self, obj):
        ordering = self.context['request'].query_params.get('ordering', None)
        tagid = self.context['request'].query_params.get('tagId', None)
        id = obj.id
        if tagid:
            next_article = Article.objects.filter(article__tag_id=tagid, id__lt=id).order_by(ordering).first()
        else:
            next_article = Article.objects.filter(id__lt=id).order_by(ordering).first()
        return ArticleTitleSerializer(next_article, many=False, context={'request': self.context['request']}).data

    class Meta:
        model = Article
        fields = ("next", "prev")

