#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Author: wg
# @Time: 18-3-10 下午3:53


from rest_framework import serializers
from home.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    """序列化"""

    class Meta:
        # 对那张表 model
        model = UserInfo
        # 只显示部分字段信息
        fields = ('id', 'username')
