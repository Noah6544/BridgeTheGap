from django.urls import path

from . import views

app_name = 'register'

urlpatterns = [
    path('',views.IndexView, name='IndexView'),
]