from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('cards/', views.card, name='card'),
    path('question-list/', views.QuestionList.as_view(), name='question_list'),
    path('topic-detail/<slug:slug>/', views.topic_detail_views, name='topic_detail'),
    path('question-detail/<slug:slug>/', views.question_detail_view, name='question_detail'),
]
