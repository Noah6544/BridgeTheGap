from django.urls import path, include
from . import views

app_name = 'course'

urlpatterns = [
    path('',views.IndexViewa, name='courseoverview_url'),
    path('Chapter/<int:chapter_id>/', views.ChapterView, name='Chapter_url'),
    path('Chapter/<int:chapter_id>/Quiz/', views.QuizView,name='Quiz_url'),
    path('Chapter/<int:chapter_id>/Quiz/Results', views.ResultsView, name='Results_url'),
    path('login_redirect',views.LoginRedirect,name='Login_redirect_url')

]