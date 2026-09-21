from django.contrib import admin
from .models import Submission


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "name",
        "email",
        "phone",
        "service",
        "created_at",
    ]

    list_filter = [
        "service",
        "created_at",
    ]

    search_fields = [
        "name",
        "email",
        "phone",
        "message",
    ]

    ordering = [
        "-created_at"
    ]
