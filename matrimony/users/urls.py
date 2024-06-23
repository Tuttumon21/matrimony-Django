from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.register, name='register'),
    path('login/',views.login, name='login'),
    path('Home/',views.Home, name='Home'),
    path('profile/',views.myprofile, name='profile'),
    # path('logout/', views.user_logout, name='logout'),
    path('login/', auth_views.LogoutView.as_view(), name='logout'),
]