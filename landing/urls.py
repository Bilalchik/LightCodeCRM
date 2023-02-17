from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('course-detail/<slug:slug>/', views.course_detail, name='course-detail')
]
