from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<char_id>[0-9]+)/$', views.charcard, name='charcard'),
]