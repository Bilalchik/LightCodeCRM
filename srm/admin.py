from django.contrib import admin
from .models import Role, Employee, Student, Expense, Income, Currency, PaymentMethod, Lead


class RoleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'cover_image', 'role', 'is_active']
    list_filter = ('created_date', 'role', 'is_active')
    search_fields = ['full_name', 'role']


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'course',
        'tariff',
        'time',
        'certificate',
        'is_graduate',
        'created_date',
        'total_payment',
        'last_payment_date']
    list_filter = ('created_date', 'course', 'tariff', 'time', 'is_graduate')
    search_fields = ['full_name', 'phone_number']


# class StudentPaymentAdmin(admin.ModelAdmin):
#     list_display = ['student', 'value', 'currency_names', 'payment_method_names', 'created_date']
#     list_filter = ('created_date', 'currency', 'payment_method')
#     search_fields = ['student', ]


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'value', 'flow_type', 'created_date']
    list_filter = ('flow_type', 'created_date')
    search_fields = ['title', ]


class IncomeAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'payment_method', 'value', 'created_date']
    list_filter = ('created_date', 'course', 'payment_method', 'course__format', 'course__studying_time', 'course__teacher')
    search_fields = ['student', ]


class LeadAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'created_date', 'is_add']
    list_filter = ('created_date', 'is_add')
    search_fields = ['full_name', 'phone_number']


admin.site.register(Role, RoleAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Currency)
admin.site.register(PaymentMethod)
admin.site.register(Lead, LeadAdmin)


