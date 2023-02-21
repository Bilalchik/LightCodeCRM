from django.contrib import admin
from .models import Role, Employee, Student, Expense, Income, Currency, PaymentMethod, Lead, Course


class RoleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'cover_image', 'role', 'is_active']
    list_filter = ('created_date', 'role', 'is_active')
    search_fields = ['full_name', 'role']


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('total_payment', 'last_payment_date')
    list_display = [
        'full_name',
        'course',
        'certificate',
        'is_graduate',
        'created_date',
        'total_payment',
        'last_payment_date']
    list_filter = ('created_date', 'course', 'is_graduate')
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
    list_display = ['student', 'payment_method', 'value', 'currency', 'created_date']
    list_filter = (
        'created_date',
        'student__course__title',
        'payment_method',
        'student__course__format',
        'student__course__studying_time',
        'student__course__teacher')
    search_fields = ['student', ]


class LeadAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'created_date', 'is_add']
    list_filter = ('created_date', 'is_add')
    search_fields = ['full_name', 'phone_number']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'studying_time', 'teacher', 'format', 'created_date', 'is_active']
    list_filter = ('studying_time', 'format', 'created_date', 'is_active')


admin.site.register(Role, RoleAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Currency)
admin.site.register(PaymentMethod)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Course, CourseAdmin)


