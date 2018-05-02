from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import HttpResponse

# Create your views here.


def index_views(request):
    # return HttpResponse('OK')
    return render(request, '01parent.html')


def child_views(request):
    return render(request, '02parent.html')


def addauthor_views(request):
    #向ｉｎｄｅｘ＿ａｕｔｈｏｒ表中增加数据
    # 1,使用第一种增加方法
    # Author.objects.create(name='noword', age=65, email='noword@163.com')
    # return HttpResponse('add ok')
    # 使用字典构建对象，并调用其save()完成增加
    # dic={
    #     'name':'trank',
    #     'age':18,
    #     'email':'hahaha@163.com',
    # }
    # obj=Author(**dic)
    # obj.save()
    # return HttpResponse('add ok')
    dic={
        'title':'macbook',
        'publicate_date':'1980-12-21',
    }
    obj = Book(**dic)
    obj.save()
    return HttpResponse('add ok')
