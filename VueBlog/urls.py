"""VueBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
import xadmin
from django.views.static import serve
from VueBlog.settings import MEDIA_ROOT, STATIC_ROOT
from django.views.generic import TemplateView
from django.conf.urls.static import static

from article.views import ArticleViewSet, PreNextViewSet
from tags.views import TagViewSet
from users.views import UserDetailViewSet
from comments.views import CommentViewSet, ReplyViewSet


router = DefaultRouter()
router.register(r'article', ArticleViewSet, base_name='article')
router.register(r'tags', TagViewSet, base_name='tags')
router.register(r'users', UserDetailViewSet, base_name='users')
router.register(r'prenext', PreNextViewSet, base_name='prenext')
router.register(r'comment', CommentViewSet, base_name='comment')
router.register(r'reply', ReplyViewSet, base_name='reply')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 富文本
    path(r'ueditor/', include('DjangoUeditor.urls')),
    # drf配置url
    path(r'docs/', include_docs_urls(title='sensu')),
    path(r'api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    # 第三方登陆
    path('', include('social_django.urls', namespace='social')),
    # 图片搜寻url
    path(r'media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    path(r'static/<path:path>', serve, {'document_root': STATIC_ROOT}),
]
