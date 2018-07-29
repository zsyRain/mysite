from django.conf.urls import url
from . import views

from django.conf import settings

from django.contrib.auth import views as  auth_views

urlpatterns = [
    #url('^login/$',views.user_login,name="user_login"),     #自定义的登录
    #url('^login/$',auth_views.login,name="user_login"),  #django内置的登录
    url('^login/$',auth_views.login,{"template_name":"account/login.html"},name="user_login"),   #django内置的登录
    url('^logout/$',auth_views.logout,{"template_name":"account/logout.html"},name="user_logout"),   #django内置的退出
    url('^register/$',views.register,name="user_register"),

    url('^password-change/$',auth_views.password_change,{"post_change_redirect":"/account/password-change-done"},name='password_change'),
    url('^password-change-done/$',auth_views.password_change_done,name='password_change_done'),

]