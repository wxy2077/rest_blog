from django.shortcuts import render
# Create your views here.

from django.views.generic.base import View

# 弃用django自带的HttpResponse
from django.http import HttpResponse

# 导入drf封装的Response
from rest_framework.response import Response

# 导入model
from article.models import Article

# 被继承的APIView
from rest_framework.views import APIView

from rest_framework import generics

# 导入关联的序列化类
from article.serializers import ArticleSerializer
from rest_framework.pagination import PageNumberPagination


#
# class ArticleListView(APIView):
#     """
#     article list 序列化  直接继承ListAPIView
#     """
#     def get(self, request, format=None):
#         article_info = Article.objects.all()
#
#         # 序列化数据
#         article_serializer = ArticleSerializer(article_info, many=True)
#
#         return Response(article_serializer.data)

class ArticlePagination(PageNumberPagination):
    """自定义分页样式"""
    page_size = 5
    page_query_param = "p"
    page_query_description = "描述...翻页参数直接用p＝页码号就行"
    max_page_size = 100


#
# class ArticleListView(generics.ListAPIView):
#     """
#     article list 序列化  直接继承ListAPIView
#     """
#     queryset = Article.objects.all()
#     # 和序列化类关联起来
#     serializer_class = ArticleSerializer
#
#     # 和分页类管理起来
#     pagination_class = ArticlePagination

from rest_framework import viewsets  # 导入viewsets视图
from rest_framework import mixins  # 导入分页的类

from .filters import ArticleFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend  # 导入关联查询字段


class ArticleListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    article list 序列化
    直接继承viewset   常用　优化路由url
    使用DefaultRouter 优化注册路由
    """
    queryset = Article.objects.all()
    # 和序列化类关联起来
    serializer_class = ArticleSerializer

    # 和分页类管理起来
    pagination_class = ArticlePagination

    # 将过滤字段关联起来
    # filter_backends = (DjangoFilterBackend,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)  # 关联　搜索字段
    filter_class = ArticleFilter            # 关联搜索的Filter类
    search_fields = ('title', 'excerpt',)   # 注意　最好不要用外键之类的　容易报错




