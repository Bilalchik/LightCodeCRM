import django_filters
from django_filters import DateFromToRangeFilter
from django import forms

from .models import Income, Expense, Student


class RangeWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        def get_widget_attrs(override=None):
            widget_attrs = {
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control',
            }
            if override:
                widget_attrs.update(override)
            return widget_attrs

        widgets = (
            forms.TextInput(attrs=get_widget_attrs({'type': 'date'})),
            forms.TextInput(attrs=get_widget_attrs()),
        )
        super(RangeWidget, self).__init__(widgets, attrs)


class DateRangeWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.widgets.DateInput(attrs={"type": "date"}),
            forms.widgets.DateInput(attrs={"type": "date"}),
        )
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(',')
        return ['', '']


class CustomDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'
    attrs = {'class': 'form-control'}

class IncomeFilter(django_filters.FilterSet):
    created_date = DateFromToRangeFilter(
        field_name='created_date',
        widget=DateRangeWidget(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Income
        fields = [
            'created_date',
            'student',
            'course',
            'payment_method',
            'course__format',
            'course__studying_time',
            'course__teacher',
            'currency']


class ExpenseFilter(django_filters.FilterSet):
    # created_date = DateFromToRangeFilter(field_name='created_date', widget=RangeWidget(
    #     attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))
    # created_date = DateFromToRangeFilter(field_name='created_date')
    created_date = DateFromToRangeFilter(
        field_name='created_date',
        widget=DateRangeWidget(attrs={'class': 'form-control', 'id': "start_date"})
    )

    class Meta:
        model = Expense
        fields = ['flow_type', 'created_date']


class StudentFilter(django_filters.FilterSet):
    # created_date = DateFromToRangeFilter(field_name='created_date', widget=RangeWidget(
    #     attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))
    # created_date = DateFromToRangeFilter(field_name='created_date', widget=RangeWidget())
    created_date = DateFromToRangeFilter(
        field_name='created_date',
        widget=DateRangeWidget(attrs={'class': 'form-control'})
    )


    class Meta:
        model = Student
        fields = [
            'course',
            'tariff',
            'is_graduate',
            'course__studying_time',
            'course__format',
            'course__teacher',
            'created_date']

