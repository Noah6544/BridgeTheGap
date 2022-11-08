from django.urls import path, include
from . import views

app_name = 'course'

urlpatterns = [
    path('',views.IndexView.as_view(), name='courseoverview_url'),
    path('Chapter/<int:chapter_id>/', views.ChapterView, name='Chapter_url'),
    path('Chapter/<int:Quiz_id>/Quiz/', views.QuizView,name='Quiz_url'),
    path('Chapter/<int:Quiz_id>/Quiz/Results', views.ResultsView, name='Results_url')

]