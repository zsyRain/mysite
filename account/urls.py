from django.conf.urls import url
from . import views

from django.conf import settings

urlpatterns = [
    #url('^login/$',views.user_login,name="user_login"),   //自定义的登录
    url('^login/$',auth_views.login,name="user_login"),
]