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

    #改密码
    url('^password-change/$',auth_views.password_change,{"post_change_redirect":"/account/password-change-done"},name='password_change'),
    url('^password-change-done/$',auth_views.password_change_done,name='password_change_done'),
    #重置密码
    url('^password-reset/$',auth_views.password_reset,{"template_name":"account/password_reset_form.html","email_template_name":"account/password_reset_email.html",
                                                       "subject_template_name":"account/password_reset_subject.txt","post_reset_redirect":"/account/password_reset_done"},
                                                        name="password_reset"),
    url('^password_reset_done/$',auth_views.password_reset_done,{"template_name":"account/password_reset_done.html"},name="password_reset_done"),
    url('^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,{"template_name":"account/password_reset_confirm.html","post_reset_redirect":"/account/password_reset_complete"},name="password_reset_confirm"),
    url('^paswoord-reset-complete/$',auth_views.password_reset_complete,{"template_name":"account/password_reset_complete.html"},name="password_reset_complete"),

    #个人信息
    url('^myself/$',views.myself,name="myself"),
    url('^myself_edit/$',views.myself_edit,name="myself_edit"),

    url('^my-image/$',views.my_image,name="my_image"),
]