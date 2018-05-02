from django.conf.urls import url,include
from .views import *

urlpatterns=[
    url(r'^$',index_views),
    url(r'^child/',child_views),
]

urlpatterns += [
    url(r'^03_addauthor/$',addauthor_views),
]