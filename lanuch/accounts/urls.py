from django.conf.urls import url
from . import views
from django.contrib.auth.views import (login, logout, password_reset, password_reset_confirm, password_reset_complete,
password_reset_done)

urlpatterns = [
    url(r'^profile/(?P<author_pk>[0-9]+)/$', views.ViewProfile, name='ProfileView'),
    url(r'^profile/edit/$', views.EditProfile, name='ProfileEdit'),
    url(r'^login/$', login, {'template_name':'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name':'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^change-password/$', views.Changepassword, name='Changepassword'),
    url(r'^reset_password/$', password_reset, name='password_reset'),
    url(r'^reset_password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset_password/complete/$', password_reset_complete, name='password_reset_complete'),
    url(r'^add/$', views.AddInfo, name='AddInfo'),

]
