from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ads.views import (
    AdsListView,
    AdsCreateView,
    AdsDetailView,
    AdsUpdateView,
    AdsDeleteView,
    AdsViewSet,
)

app_name = "ads"

routers = DefaultRouter()
routers.register("", AdsViewSet)

urlpatterns = [
    path("", AdsListView.as_view(), name="ads_list"),
    path("api/", include(routers.urls)),
    path("new/", AdsCreateView.as_view(), name="ads_create"),
    path("<int:pk>/", AdsDetailView.as_view(), name="ads_detail"),
    path("<int:pk>/edit/", AdsUpdateView.as_view(), name="ads_update"),
    path("<int:pk>/delete/", AdsDeleteView.as_view(), name="ads_delete"),
]
