from django.contrib import admin
from .models import Course, Review, StudyingTime, LearningFormat


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'studying_time_names', 'teacher', 'format_names', 'created_date', 'is_active']
    list_filter = ('studying_time', 'format', 'created_date', 'is_active')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Course, CourseAdmin)
admin.site.register(Review)
admin.site.register(StudyingTime)
admin.site.register(LearningFormat)
