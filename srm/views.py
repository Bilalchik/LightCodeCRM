from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView

from .forms import LeadForm, StudentForm, IncomeForm, ExpenseForm
from .filters import IncomeFilter, ExpenseFilter, StudentFilter
from .models import Lead, Student, Income, Expense


def leads_view(request):
    leads = Lead.objects.all().order_by('-id')
    students = Student.objects.all().order_by('-id')
    return render(request, template_name='srm/leads.html', context={'leads': leads, 'students': students})


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context


class StudentListView(FilteredListView):
    model = Student
    queryset = Student.objects.all().order_by('-id')
    filterset_class = StudentFilter
    template_name = 'srm/leads.html'
    context_object_name = 'students'


def lead_add(request):
    if request.method == 'POST':
        form = LeadForm(data=request.POST)
        if form.is_valid():
            lead = form.save()
            return redirect('students')

    form = LeadForm()
    return render(request, template_name='srm/lead_add.html', context={'form': form})


def leads_detail(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads')
    else:
        form = LeadForm(instance=lead)

    return render(request, template_name='srm/leads_detail.html', context={'lead': lead, 'form': form})


def lead_delete(request, pk):

    lead = Lead.objects.get(id=pk)
    lead.delete()

    return HttpResponseRedirect(reverse('leads'))


def student_list(request):
    leads = Lead.objects.all().order_by('-id')

    return render(request, template_name='srm/students.html', context={
        'leads': leads})


def student_detail(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('leads')
    else:
        form = StudentForm(instance=student)

    return render(request, template_name='srm/student_detail.html', context={'student': student, 'form': form})


def student_delete(request, pk):

    student = Student.objects.get(id=pk)
    student.delete()

    return HttpResponseRedirect(reverse('leads'))


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            lead = form.save()
            return redirect('leads')

    form = StudentForm()
    return render(request, template_name='srm/student_add.html', context={'form': form})

class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context


class IncomeListView(FilteredListView):
    model = Income
    queryset = Income.objects.all().order_by('-id')
    filterset_class = IncomeFilter
    template_name = 'srm/incomes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expense = Expense.objects.all().order_by('-id')
        filterset_expense = ExpenseFilter(self.request.GET, queryset=expense, prefix='expense')

        context['gg'] = filterset_expense
        context['kaka'] = expense
        context['expenses'] = filterset_expense.qs
        context['total_incomes'] = context['object_list'].aggregate(total=Sum('value'))['total']
        context['total_expenses'] = context['expenses'].aggregate(total=Sum('value'))['total']
        if context['total_incomes'] and context['total_expenses']:
            context['net_profit'] = context['object_list'].aggregate(total=Sum('value'))['total'] - context['expenses'].aggregate(total=Sum('value'))['total']

        return context


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context

class Debtor(FilteredListView):
    model = Student
    queryset = Student.objects.all().order_by('-id')
    filterset_class = StudentFilter
    template_name = 'srm/debtors.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_debtors'] = context['students'].aggregate(total=Sum('remainder'))['total']
        return context


def income_detail(request, pk):
    income = get_object_or_404(Income, id=pk)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm(instance=income)

    return render(request, template_name='srm/income_detail.html', context={'income': income, 'form': form})


def income_add(request):
    if request.method == 'POST':
        form = IncomeForm(data=request.POST)
        if form.is_valid():
            lead = form.save()
            return redirect('income_list')

    form = IncomeForm()
    return render(request, template_name='srm/income_add.html', context={'form': form})


def income_delete(request, pk):

    income = Income.objects.get(id=pk)
    income.delete()

    return HttpResponseRedirect(reverse('income_list'))


class ExpenseListView(FilteredListView):
    model = Expense
    queryset = Expense.objects.all().order_by('-id')
    filterset_class = ExpenseFilter
    template_name = 'srm/expenses_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = context['object_list'].aggregate(total=Sum('value'))['total']

        return context


def expense_detail(request, pk):
    expense = get_object_or_404(Expense, id=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, template_name='srm/expense_detail.html', context={'expense': expense, 'form': form})


def expense_add(request):
    if request.method == 'POST':
        form = ExpenseForm(data=request.POST)
        if form.is_valid():
            lead = form.save()
            return redirect('income_list')

    form = ExpenseForm()
    return render(request, template_name='srm/expense_add.html', context={'form': form})


def expense_delete(request, pk):

    expense = Expense.objects.get(id=pk)
    expense.delete()

    return HttpResponseRedirect(reverse('income_list'))


def personal(request):
    return render(request, template_name='srm/personal.html')


def manager(request):
    leads = Lead.objects.all()
    lead_count = leads.count()
    student = Student.objects.all()
    student_count = student.count()
    return render(request, template_name='srm/manager.html', context={
        'lead_count': lead_count,
        'student_count': student_count})


def admin_choice(request):
    return render(request, template_name='srm/admin_choice.html')


