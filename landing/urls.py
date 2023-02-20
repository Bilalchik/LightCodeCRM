from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('course-detail/<slug:slug>/', views.course_detail, name='course-detail'),
    path('employee_detail/<int:pk>/', views.employee_detail, name='employee_detail')
]
