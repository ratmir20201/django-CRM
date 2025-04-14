from django.contrib import admin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "lead",
        "contract",
    )
    list_display_links = "pk", "lead"
    ordering = ("pk",)
    search_fields = ("lead",)
