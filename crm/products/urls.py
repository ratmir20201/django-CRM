from django.urls import path

from products.views import (
    ProductsListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = "products"

urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list"),
    path("new/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
