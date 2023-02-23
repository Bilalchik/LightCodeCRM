from django import forms
from .models import Lead, Student, Income, Expense, Course, Employee
from django_select2 import forms as s2forms


class StudentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "full_name__icontains",
    ]


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['full_name', 'phone_number', 'course', 'is_add', 'description']


class StudentForm(forms.ModelForm):
    last_payment_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
        required=False
    )
    remainder = forms.DecimalField(label='Общая оплата за курс')

    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'course', 'teacher', 'studying_time', 'format', 'certificate', 'url', 'is_graduate', 'remainder', 'description']


class IncomeForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=StudentWidget
    )
    date_of_payment = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
        label='Дата оплаты'
    )

    class Meta:
        model = Income
        fields = ['student', 'value', 'payment_method', 'currency', 'date_of_payment']
        # widgets = {
        #     "student": StudentWidget,
        # }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'value', 'flow_type']
