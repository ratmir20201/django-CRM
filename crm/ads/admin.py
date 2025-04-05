from django.contrib import admin

from ads.models import Ads


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "product", "channel", "formatted_budget"
    list_display_links = "pk", "name"
    ordering = ("pk",)
    search_fields = ("name",)

    def formatted_budget(self, obj):
        return f"{obj.budget:,.2f}"

    formatted_budget.short_description = "Бюджет (в руб)"
