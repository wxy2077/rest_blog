#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Author: wg
# @Time: 18-3-14 上午11:27
# @Describe: 过滤字段

import django_filters
from django.db.models import Q

from .models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):
    """
    文章的过滤类
    """
    # 文章点击量
    click_min = django_filters.NumberFilter(name='on_click', help_text="最低点击量", lookup_expr='gte')
    click_max = django_filters.NumberFilter(name='on_click', help_text="最高点击量", lookup_expr='lte')

    class Meta:
        model = Article
        fields = ['click_min', 'click_max']
