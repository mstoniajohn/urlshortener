from django.urls import path
# from django.contrib.auth.views import login, logout
from . import views
urlpatterns = [
    path('login', views.login_view, name='login' ),
    path('register/', views.register, name='register'),
    path('logout_view/', views.logout_view, name='logout'),



]
