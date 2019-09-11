from django.db import models


# Create your models here.
class TagCategory(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名称")
    desc = models.TextField(max_length=500, verbose_name="分类描述")

    class Meta:
        verbose_name = "标签分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    cid = models.ForeignKey(TagCategory, verbose_name="标签", on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name="标签名称")
    is_index = models.BooleanField(default=False, verbose_name="是否指标")
    is_show = models.BooleanField(default=False, verbose_name="是否展示")
    sort = models.IntegerField(default=1, verbose_name="排序")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
