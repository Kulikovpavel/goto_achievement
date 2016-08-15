from django.contrib import admin

from main.models import Achievement, Student, Record


class StudentAdmin(admin.ModelAdmin):
    model = Student
    search_fields = ('lastname', 'firstname',)
    list_filter = ('group',)


admin.site.register(Achievement)
admin.site.register(Student, StudentAdmin)
admin.site.register(Record)
