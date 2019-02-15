"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
# from django.contrib import admin
import xadmin

from rest_framework.documentation import include_docs_urls

from home.views import IndexView

# from .settings import MEDIA_ROOT
from blog.settings import MEDIA_ROOT  # 访问上传的文件路径
from django.views.static import serve


# 使用DefaultRouter  来注册路由更方便
from rest_framework.routers import DefaultRouter

# 导入文章app下面的类视图函数
from article.views import ArticleListViewSet

# article_list = ArticleListViewSet.as_view({
#     'get': 'list',    # 定义请求方法
#     # 'post': 'create'
# })
router = DefaultRouter()
# 注册路由
router.register(r'article', ArticleListViewSet)


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 添加前后端分离　　可见视图的url
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 网站url
    url(r'^$', IndexView.as_view(), name="index"),

    # 添加文章首页url
    # url(r'^article/', ArticleListView.as_view(), name="article_info"),
    # url(r'^article/', article_list, name="article_info"),    # 使用viewset去优化路由
    url(r'^', include(router.urls)),   # 使用使用DefaultRouter来注册路由更方便
    # 添加富文本url
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),

    # 添加文档路由
    url(r'docs/', include_docs_urls(title="个人博客")),
]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
