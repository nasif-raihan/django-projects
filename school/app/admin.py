from django.contrib import admin

from .models import Grade, Student, Subject, Teacher, MarkSheet


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("remark",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "credit")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "group", "teacher")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject")


@admin.register(MarkSheet)
class MarkSheetAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "grade")
