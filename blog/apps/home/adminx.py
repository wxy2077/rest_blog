#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Author: wg
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import UserInfo, Banner


# ----- adminx 全局配置
class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = '个人博客后台管理系统'
    site_footer = '我的xadmin'
    menu_style = 'accordion'
# ------


class UserInfoAdmin(object):

    # 页面中显示的选项
    list_display = ['id', 'nick_name', 'birthday', 'gender', 'mobile', 'email', 'add_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


'''
 直接修改 xadmin 的源码，即 xadmin/plugins/auth.py 里添加这两行代码
from django.contrib.auth import get_user_model
User = get_user_model()
 就可以代替下面那段代码
'''
# ---
# class UserProfileAdmin(UserAdmin):
#     pass


# 卸载 django 自带的 auth_user
# from django.contrib.auth.models import User
# xadmin.site.unregister(User)


# 继承自定义的 UserProfile 覆盖 django 自带的 auth_user
# xadmin.site.register(UserProfile, UserProfileAdmin)
# --

# xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)


