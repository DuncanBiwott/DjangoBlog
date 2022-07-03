from django import views
from django.urls import path
from .import views

urlpatterns = [
    path('',views.blog_post,name='blog'),

    path('search/',views.search,name='search'),
    path('profile/',views.profile,name='profile'),
    path('blog_comments/<str:slug>',views.blog_comments,name='blog_comments'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('user_posts/<str:myid>/',views.user_posts,name='user_posts'),
    path('delete_post/<str:slug>/',views.delete_post,name='delete_post'),
    path('add_post/',views.add_post,name='add_post'),



    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]
