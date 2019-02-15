from django.db import models
from datetime import datetime
# Create your models here.
# 继承django的基本用户model
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    """
    用户
    """
    nick_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='昵称')
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female",
                              verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        db_table = "userinfo"


class Banner(models.Model):
    """轮播图"""
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', max_length=100, verbose_name='轮播图')
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')

    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
