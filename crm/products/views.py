from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from products.forms import ProductForm
from products.models import Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = "products/products-create.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products:products_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "products/products-edit.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse(
            "products:product_details",
            kwargs={"pk": self.object.pk},
        )


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "products/products-delete.html"
    model = Product
    success_url = reverse_lazy("products:products_list")


class ProductsListView(LoginRequiredMixin, ListView):
    template_name = "products/products-list.html"
    model = Product
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = "products/products-detail.html"
    model = Product
    context_object_name = "object"
