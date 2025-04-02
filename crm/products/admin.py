from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "short_description", "price"
    list_display_links = "pk", "name"
    ordering = ("pk",)
    search_fields = "name", "description"

    @staticmethod
    def short_description(obj: Product):
        if len(obj.description) < 80:
            return obj.description
        return obj.description[:80] + "..."
