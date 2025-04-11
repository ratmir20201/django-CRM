from django.contrib import admin

from leads.models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "first_name",
        "last_name",
        "phone",
        "email",
        "ad",
    )
    list_display_links = "pk", "first_name", "last_name"
    ordering = ("pk",)
    search_fields = "first_name", "last_name"
