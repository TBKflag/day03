from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.db.models import F,Q


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
    dic={
        'name':'trank',
        'age':18,
        'email':'hahaha@163.com',
    }
    obj=Author(**dic)
    obj.save()
    return HttpResponse('add ok')
    # dic={
    #     'title':'travisbook',
    #     'publicate_date':'2020-12-21',
    # }
    # obj = Book(**dic)
    # obj.save()
    # return HttpResponse('add ok')


def authorrall_views(request):
    #查询ａｕｔｈｏｒ实体中所有的数据
    # authors=Author.objects.all()
    # # print(authors)
    # for au in authors:
    #     print(au.name+',',au.age,','+au.email)
    # return HttpResponse('query ok')
    #通过ｖａｌｕｅｓ查询部分列的数据
    # authors=Author.objects.values('name','age')
    # for au in authors:
    #     print(au['name']+',', au['age'])
    #通过order_by实现排序
    # authors = Author.objects.order_by('-age')
    # for au in authors:
    #     print(au.name+',', au.age, au.email)
    # return HttpResponse('query ok')

    # 通过ｅｘｃｌｕｄｅ()实现条件取反
    authors=Author.objects.filter(age=18)
    # 使用__ｃｏｎｔａｉｎｓ查询
    authors=Author.objects.filter(email__contains='d')
    print('----------------------------------------')
    for au in authors:
        print(au.name, au.age, au.email)
    return HttpResponse('query ok')


def all_views(request):
    authors=Author.objects.all()
    #locals函数可以把所有的变量封装成字典
    return render(request, '03_author.html', locals())
    # au = Author.objects.get(id=1)
    # au.name = '王宝强'
    # au.age = 35
    # au.save()
    # return HttpResponse('ok')


def delete_views(request, aid):
    author=Author.objects.get(id=aid)
    author.isactive=False
    author.save()
    # return HttpResponse('删除成功')
    #使用转发跳转到　all_views() 视图
    # return all_views(request)
    # 重定向,需要导入httpresponseRedirect
    # 重新定向到０５＿ａｌｌ
    return HttpResponseRedirect('/05_all/')


def change_views(request, id):
    author=Author.objects.get(id=id)
    print(author.age)
    return render(request, '04_au.html', locals())

def doF_views(request):
    Author.objects.all().update(age=F('age')+10)
    return HttpResponse('ok')

def doQ_views(request):
    authors=Author.objects.filter(Q(id=2)|Q(age__gte=15))
    return render(request, '03_author.html',locals())

def oto_views(request):
    w=wife.objects.get(id=3)
    a=w.author
    return render(request,'05_oto.html',locals())


def otm_views(request):
    # 通过书籍查询对应的ｐｕｂｌｉｈｓｅｒ
    b=Book.objects.get(id=8)
    publisher=b.publisher
    # return render(request,'06_otm.html',locals())
    # 通过ｐｕｂｌｉｓｈｅｒ查询对应的所有ｂｏｏｋ
    pub = Publisher.objects.get(id=3)
    books=pub.book_set.all()
    print(books)
    return render(request, '06_otm.html', locals())


def mtm_views(request):
    # 正向查询
    book = Book.objects.get(id=9)
    authors = book.author.all()
    # 反向查询
    author = Author.objects.get(id=3)
    books = author.book_set.all()

    return render(request, '07mtm.html', locals())

def aucount_views(request):
    # return HttpResponse(Author.objects.aucount(25))
    return HttpResponse(Book.objects.title_count('o'))