from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "short_description", "formatted_price"
    list_display_links = "pk", "name"
    ordering = ("pk",)
    search_fields = "name", "description"

    def short_description(self, obj: Product):
        if len(obj.description) < 80:
            return obj.description
        return obj.description[:80] + "..."

    def formatted_price(self, obj):
        return f"{obj.price:,.2f}"

    short_description.short_description = "Описание"
    formatted_price.short_description = "Цена (в руб)"
