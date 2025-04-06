from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import (
    ProductsListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductViewSet,
)

app_name = "products"

routers = DefaultRouter()
routers.register("", ProductViewSet)


urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list"),
    path("api/", include(routers.urls)),
    path("new/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
