from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.access_list, name='access_list'),
    url(r'^access-detail/(?P<pk>\d+)/$', views.access_detail, name='access_detail'),
    url(r'^access_new/$', views.access_new, name='access_new'),
    url(r'^access/(?P<pk>\d+)/edit/$', views.access_edit, name='access_edit'),
]