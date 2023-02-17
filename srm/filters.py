import django_filters
from django_filters import DateFromToRangeFilter

from .models import Income, Expense


class IncomeFilter(django_filters.FilterSet):
    # genres = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all())
    created_date = DateFromToRangeFilter(field_name='created_date')

    class Meta:
        model = Income
        fields = ['created_date', 'course', 'payment_method', 'course__format', 'course__studying_time', 'course__teacher']


class ExpenseFilter(django_filters.FilterSet):
    created_date = DateFromToRangeFilter(field_name='created_date')

    class Meta:
        model = Expense
        fields = ['flow_type', 'created_date']


