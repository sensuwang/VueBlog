from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField

from tags.models import Tag
from users.models import UserProfile


# Create your models here.
class Article(models.Model):
    """
    文章
    """

    STATUS_TYPE = (
        (0, "草稿"),
        (1, "发布"),
    )

    author_id = models.ForeignKey(UserProfile, verbose_name="作者", on_delete=models.CASCADE)
    title = models.CharField(default="", max_length=200, verbose_name="标题")
    content = UEditorField(verbose_name=u"文章内容", imagePath="article/images/", width=1000, height=300,
                              filePath="article/files/", default='')
    visit_count = models.IntegerField(default=0, verbose_name="浏览数")
    comment_count = models.IntegerField(default=0, verbose_name="评论数")
    top = models.BooleanField(default=False, verbose_name="是否置顶")
    status = models.IntegerField(choices=STATUS_TYPE, verbose_name="文章状态")
    created = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    publish_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    updated = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "文章信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    """
    文章图片
    """
    article = models.ForeignKey(Article, verbose_name="文章", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '文章图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.title


class ArticleTag(models.Model):
    """
    文章标签
    """
    article = models.ForeignKey(Article, verbose_name="文章", related_name="article", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, verbose_name="标签名称", related_name="tags", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name
        unique_together = ("article", "tag")

    def __str__(self):
        return self.article.title
