from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^transaction', views.post, name='transaction'),
    url(r'export',views.export,name='export')


]