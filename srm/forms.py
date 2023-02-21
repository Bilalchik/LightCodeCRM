from django import forms
from .models import Lead, Student, Income, Expense
from django_select2 import forms as s2forms


class StudentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "full_name__icontains",
    ]


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['full_name', 'phone_number', 'course', 'description', 'is_add']


class StudentForm(forms.ModelForm):
    last_payment_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'course', 'certificate', 'url', 'is_graduate']


class IncomeForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=StudentWidget
    )

    class Meta:
        model = Income
        fields = ['student', 'value', 'payment_method', 'currency']
        # widgets = {
        #     "student": StudentWidget,
        # }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'value', 'flow_type']
