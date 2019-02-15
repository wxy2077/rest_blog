from django.shortcuts import render

from django.views.generic.base import View
from django.http import HttpResponse
# Create your views here.


# 个人博客首页
class IndexView(View):
    def get(self, request):
        return HttpResponse("hello world")


