from django.contrib import admin


# 弃用  改用xadmin
# Register your models here.
# from home.models import UserInfo
#
#
# class UserInfoAdmin(admin.ModelAdmin):
#
#     # 页面中显示的选项
#     list_display = ['id', 'nick_name', 'birthday', 'gender', 'mobile', 'email', 'add_time']
#     # 每页显示的条数
#     list_per_page = 10
#     pass
#
#
# # 注册到管理后台
# admin.site.register(UserInfo, UserInfoAdmin)