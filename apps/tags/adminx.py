__author__ = 'sensuu'
__date__ = '2019/5/12 13:16'
import xadmin

from .models import Tag, TagCategory


class TagCategoryAdmin(object):
    list_diaplay = ["name", "desc"]


class TagAdmin(object):
    list_diaplay = ["cid", "name", "is_index", "is_show", "sort"]


xadmin.site.register(TagCategory, TagCategoryAdmin)
xadmin.site.register(Tag, TagAdmin)


