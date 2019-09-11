from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    """
    用户
    """
    nick_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    mobile = models.CharField(blank=True, null=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    avatar = models.TextField(max_length=100, null=True, blank=True, verbose_name="头像")
    is_active = models.BooleanField(default=True, verbose_name="是否激活")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
