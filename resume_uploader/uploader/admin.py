from django.contrib import admin

from .models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "birth_date",
        "gender",
        "nationality",
        "division",
        "city",
        "postal_code",
        "mobile",
        "email",
        "profile_photo",
        "resume_file",
    )
