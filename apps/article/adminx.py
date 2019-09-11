__author__ = 'sensuu'
__date__ = '2019/5/12 10:58'
import xadmin

from .models import ArticleImage, ArticleTag, Article


class ArticleAdmin(object):
    list_display = ["author_id", "title", "visit_count", "comment_count", "status"]
    style_fields = {"content": "ueditor"}

    class ArticleImageInline(object):
        model = ArticleImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [ArticleImageInline]


class ArticleTagAdmin(object):
    list_display = ["article", "tag"]


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ArticleTag, ArticleTagAdmin)
