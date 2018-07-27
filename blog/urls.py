from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.blog_title,name="blog_title"),
]