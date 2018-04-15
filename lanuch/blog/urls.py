from django.conf.urls import url
from . import views
app_name='blog'
urlpatterns = [
    url(r'^$', views.Post_all, name='home'),
    url(r'^(?P<post_pk>[0-9]+)/$', views.Post_detail, name='detail'),
    url(r'^create/$', views.Post_create, name='CreatePost'),
    url(r'^create/comment/(?P<post_pk>[0-9]+)/$', views.CreateComment, name='CreateComment'),
    url(r'^delete/comment/(?P<post_pk>[0-9]+)/$', views.DeleteComment, name='DeleteComment'),
    url(r'^delete/(?P<post_pk>[0-9]+)/$', views.Post_delete, name='Post_delete'),

]
