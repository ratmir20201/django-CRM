from django.urls import path

from ads.views import (
    AdsListView,
    AdsCreateView,
    AdsDetailView,
    AdsUpdateView,
    AdsDeleteView,
)

app_name = "ads"

urlpatterns = [
    path("", AdsListView.as_view(), name="ads_list"),
    path("new/", AdsCreateView.as_view(), name="ads_create"),
    path("<int:pk>/", AdsDetailView.as_view(), name="ads_details"),
    path("<int:pk>/edit/", AdsUpdateView.as_view(), name="ads_update"),
    path("<int:pk>/delete/", AdsDeleteView.as_view(), name="ads_delete"),
]
