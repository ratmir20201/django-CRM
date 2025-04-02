from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "description", "price"
        labels = {
            "name": "Название",
            "description": "Описание",
            "price": "Цена (в руб)",
        }
        widgets = {"description": forms.Textarea(attrs={"rows": 5})}
