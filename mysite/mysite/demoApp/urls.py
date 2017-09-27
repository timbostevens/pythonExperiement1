from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dataEntry', views.dataEntry, name='dataEntry'),
    url(r'^dataDisplay', views.dataDisplay, name='dataDisplay'),
    url(r'^inputView', views.inputView, name='inputView'),
]