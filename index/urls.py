from django.conf.urls import url,include
from .views import *

urlpatterns=[
    url(r'^$',index_views),
    url(r'^child/',child_views),
]

urlpatterns += [
    url(r'^03_addauthor/$',addauthor_views),
    url(r'04_all/$',authorrall_views),
    url(r'^05_all/$',all_views),
    url(r'^del/(\d)*/$', delete_views,name='del'),
]
