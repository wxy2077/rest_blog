#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Author: wg

import xadmin
from xadmin import views
# from xadmin.plugins.auth import UserAdmin
from .models import Category, Tag, Article


# ----- adminx 全局配置
# class BaseSetting:
#     enable_themes = True
#     use_bootswatch = True
#
#
# class GlobalSettings:
#     site_title = '个人博客后台管理系统'
#     site_footer = '我的xadmin'
#     menu_style = 'accordion'
# ------


class CategoryAdmin(object):
    # 页面中显示的选项
    list_display = ['name']


class TagAdmin(object):
    list_display = ['name']


class ArticleAdmin(object):
    list_display = ['title', 'add_time', 'category', 'tags', 'on_click', 'comment_num']
    search_fields = ['title', 'create_time', 'category', 'tags']
    list_filter = ['title', 'add_time', 'category', 'tags', 'on_click', 'comment_num']
    # 注意这里是content是你要换成ueditor的字段
    style_fields = {'content': 'ueditor'}


# class SinginAdmin(object):
#     list_display = ['create_time', 'user', 'address']
#     search_fields = ['user']
#     list_per_page = 10


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Article, ArticleAdmin)





