from django.urls import path, include
from . import views

app_name = 'Users'

urlpatterns = [
    path('profile/',views.IndexView, name='profile_url'),
    path('login/', views.Login, name='Login_url'),
    path('register/',views.Register,name='Register_url'),
    path('logout/',views.Logout,name='Logout_url'),
]