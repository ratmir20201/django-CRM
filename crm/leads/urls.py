from django.urls import path, include
from rest_framework.routers import DefaultRouter

from leads.views import (
    LeadsListView,
    LeadCreateView,
    LeadDetailView,
    LeadUpdateView,
    LeadDeleteView,
    LeadViewSet,
)

app_name = "leads"

routers = DefaultRouter()
routers.register("", LeadViewSet)

urlpatterns = [
    path("", LeadsListView.as_view(), name="leads_list"),
    path("api/", include(routers.urls)),
    path("new/", LeadCreateView.as_view(), name="lead_create"),
    path("<int:pk>/", LeadDetailView.as_view(), name="lead_detail"),
    path("<int:pk>/edit/", LeadUpdateView.as_view(), name="lead_update"),
    path("<int:pk>/delete/", LeadDeleteView.as_view(), name="lead_delete"),
]
