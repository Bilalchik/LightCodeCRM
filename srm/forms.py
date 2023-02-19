from django import forms
from .models import Lead, Student, Income, Expense


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['full_name', 'phone_number', 'course', 'description', 'is_add']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'course', 'tariff', 'certificate', 'url', 'time', 'is_graduate', 'total_payment', 'last_payment_date']


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['student', 'course', 'value', 'payment_method', 'currency']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'value', 'flow_type']
