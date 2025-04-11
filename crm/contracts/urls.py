from django.urls import path, include
from rest_framework.routers import DefaultRouter

from contracts.views import (
    ContractViewSet,
    ContractsListView,
    ContractCreateView,
    ContractDetailView,
    ContractDeleteView,
    ContractUpdateView,
)

app_name = "contracts"

routers = DefaultRouter()
routers.register("", ContractViewSet)

urlpatterns = [
    path("", ContractsListView.as_view(), name="contracts_list"),
    path("api/", include(routers.urls)),
    path("new/", ContractCreateView.as_view(), name="contract_create"),
    path("<int:pk>/", ContractDetailView.as_view(), name="contract_detail"),
    path("<int:pk>/edit/", ContractUpdateView.as_view(), name="contract_update"),
    path("<int:pk>/delete/", ContractDeleteView.as_view(), name="contract_delete"),
]
