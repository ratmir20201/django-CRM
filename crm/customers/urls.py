from django.urls import path, include
from rest_framework.routers import DefaultRouter

from customers.views import (
    CustomersListView,
    CustomerCreateView,
    CustomerDetailView,
    CustomerUpdateView,
    CustomerDeleteView,
    CustomerViewSet,
)

app_name = "customers"

routers = DefaultRouter()
routers.register("", CustomerViewSet)

urlpatterns = [
    path("", CustomersListView.as_view(), name="customers_list"),
    path("api/", include(routers.urls)),
    path("new/", CustomerCreateView.as_view(), name="customer_create"),
    path("<int:pk>/", CustomerDetailView.as_view(), name="customer_detail"),
    path("<int:pk>/edit/", CustomerUpdateView.as_view(), name="customer_update"),
    path("<int:pk>/delete/", CustomerDeleteView.as_view(), name="customer_delete"),
]
