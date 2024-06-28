from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.register, name='register'),
    path('login/',views.login, name='login'),
    path('Home/',views.Home, name='Home'),
    path('profile/',views.myprofile, name='profile'),
    # path('', views.user_logout, name='logout'),
    path('login/', auth_views.LogoutView.as_view(), name='logout'),

    path('profile/', views.profile_detail_view, name='profile_detail'),
    path('profile/edit/', views.profile_update_view, name='profile_update'),
    path('profile/create/', views.profile_create_view, name='profile_create'),
]