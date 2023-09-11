from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("<int:article_id>/", get_article, name='get_article'),
    path("auth/", auth, name='auth'),
    path("back/", back, name='back'),
    path("register/", register, name='register'),
    path("", blog_list, name='blog_list'),
    path("add_article/", add_article, name='add_article'),
    path("logout/", logout_page, name='logout'),
    path("mypage/", my_page, name='my_page'),
    path("id<int:user_profile_id>/", index, name="index"),
]