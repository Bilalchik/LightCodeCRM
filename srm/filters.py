import django_filters
from django_filters import DateFromToRangeFilter

from .models import Income, Expense, Student


class IncomeFilter(django_filters.FilterSet):
    # genres = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all())
    created_date = DateFromToRangeFilter(field_name='created_date')

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
    created_date = DateFromToRangeFilter(field_name='created_date')

    class Meta:
        model = Expense
        fields = ['flow_type', 'created_date']


class StudentFilter(django_filters.FilterSet):
    created_date = DateFromToRangeFilter(field_name='created_date')

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

