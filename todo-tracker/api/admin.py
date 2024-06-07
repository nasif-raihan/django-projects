from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
        "updated_at",
        "is_completed",
        "created_by",
    ]