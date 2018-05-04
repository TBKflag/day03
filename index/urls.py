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
    url(r'^change/(\d)*/$',change_views,name='change'),
    url(r'^updatedb/', update_db),
    url(r'08doF', doF_views),
    url(r'10_doQ',doQ_views),
    url(r'11_oto/', oto_views),
    url(r'12_otm/',otm_views),
    url(r'^13_mtm/$',mtm_views),
    url(r'14count/', aucount_views)
]
