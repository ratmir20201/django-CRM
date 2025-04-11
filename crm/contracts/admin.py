from django.contrib import admin

from contracts.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "product",
        "document",
        "start_date",
        "end_date",
        "formatted_cost",
    )
    list_display_links = "pk", "name"
    ordering = ("pk",)
    search_fields = ("name",)

    def formatted_cost(self, obj):
        return f"{obj.cost:,.2f}"

    formatted_cost.short_description = "Сумма (в руб)"
