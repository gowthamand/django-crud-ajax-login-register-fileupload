from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^list$', views.list, name='list'),
    url(r'^fileupload$', views.fileupload, name='fileupload'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^ajax/ajax$', views.ajax, name='ajaxpost'),
    url(r'^ajax/delete$', views.ajax_delete, name='ajax_delete'),
    url(r'^ajax/getajax$', views.getajax, name='getajax'),
    url(r'^register/$', views.register,name='register'),
    url(r'^register/success/$',views.register_success,name='register_success'),
]