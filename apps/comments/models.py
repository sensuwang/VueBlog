from datetime import datetime

from django.db import models

from article.models import Article
from users.models import UserProfile


# Create your models here.
class Comment(models.Model):
    """
    评论
    """
    # STATUS_TYPE = (
    #     (0, "删除"),
    #     (1, "正常")
    # )

    aid = models.ForeignKey(Article, verbose_name="文章", on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    content = models.TextField(max_length=500, verbose_name="评论内容")
    # status = models.IntegerField(choices=STATUS_TYPE, verbose_name="评论状态")
    created = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    updated = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "评论信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{user}({article})'.format(user=self.user_id.username, article=self.aid.title)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name="replys", verbose_name="评论回复", on_delete=models.CASCADE)
    user_info = models.ForeignKey(UserProfile, related_name="user_info", verbose_name="用户信息", on_delete=models.CASCADE)
    content = models.TextField(max_length=500, verbose_name="回复内容")
    created = models.DateTimeField(default=datetime.now, verbose_name="回复时间")

    class Meta:
        verbose_name = "回复评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}({comment})".format(user=self.user_info.username, comment=self.comment.content)

