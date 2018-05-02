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
        'title':'travisbook',
        'publicate_date':'2020-12-21',
    }
    obj = Book(**dic)
    obj.save()
    return HttpResponse('add ok')


def authorrall_views(request):
    #查询ａｕｔｈｏｒ实体中所有的数据
    # authors=Author.objects.all()
    # # print(authors)
    # for au in authors:
    #     print(au.name+',',au.age,','+au.email)
    # return HttpResponse('query ok')
    #通过ｖａｌｕｅｓ查询部分列的数据
    authors=Author.objects.values('name','age')
    for au in authors:
        print(au['name']+',', au['age'])
    return HttpResponse('query ok')
