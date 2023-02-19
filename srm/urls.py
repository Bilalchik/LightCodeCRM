from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentListView.as_view(), name='leads'),
    path('', views.personal, name='personal'),
    path('leads_add/', views.lead_add, name='lead_add'),
    path('leads/<int:pk>/', views.leads_detail, name='leads_detail'),
    path('leads/delete/<int:pk>', views.lead_delete, name='lead_delete'),
    path('leads/', views.student_list, name='students'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('students_add/', views.student_add, name='student_add'),
    path('administrator/', views.IncomeListView.as_view(), name='income_list'),
    path('income_detail/<int:pk>/', views.income_detail, name='income_detail'),
    path('income_add/', views.income_add, name='income_add'),
    path('income_list/delete/<int:pk>/', views.income_delete, name='income_delete'),
    # path('expenses_list/', views.ExpenseListView.as_view(), name='expenses_list'),
    path('expense_detail/<int:pk>/', views.expense_detail, name='expense_detail'),
    path('expense_add/', views.expense_add, name='expense_add'),
    path('expense_delete/<int:pk>', views.expense_delete, name='expense_delete'),
    path('manager/', views.manager, name='manager'),
    path('debtor/', views.Debtor.as_view(), name='debtor'),
    path('admin_choice/', views.admin_choice, name='admin_choice'),
]
