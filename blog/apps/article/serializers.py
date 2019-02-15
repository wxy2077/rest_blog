#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Author: wg
# @Time: 18-3-10 下午3:54

from rest_framework import serializers
from article.models import Article, Category, Tag
from home.serializers import UserInfoSerializer


class CategorySerializer(serializers.ModelSerializer):
    """序列化"""
    class Meta:
        # 对那张表 model
        model = Category
        # 那些字段
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    """序列化"""

    class Meta:
        # 对那张表 model
        model = Tag
        # 那些字段
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    """序列化"""
    # 直接把外键信息显示出来
    category = CategorySerializer()
    tags = TagSerializer()
    author = UserInfoSerializer()

    class Meta:
        # 对那张表 model
        model = Article
        # 那些字段
        fields = "__all__"
