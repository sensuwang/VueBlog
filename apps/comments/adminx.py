__author__ = 'sensuu'
__date__ = '2019/5/26 21:47'
import xadmin

from .models import Comment, Reply


class CommentAdmin(object):
    list_display = ["aid", "user_id", "content", "created", "updated"]


class ReplayAdmin(object):
    list_display = ["comment", "user_info", "content", "created"]


xadmin .site.register(Comment, CommentAdmin)
xadmin .site.register(Reply, ReplayAdmin)
