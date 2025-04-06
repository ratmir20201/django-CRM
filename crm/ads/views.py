from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from ads.forms import AdsForm
from ads.models import Ads


class AdsListView(LoginRequiredMixin, ListView):
    template_name = "ads/ads-list.html"
    queryset = Ads.objects.select_related("product")
    context_object_name = "ads"


class AdsDetailView(LoginRequiredMixin, DetailView):
    template_name = "ads/ads-detail.html"
    model = Ads
    context_object_name = "object"


class AdsCreateView(LoginRequiredMixin, CreateView):
    template_name = "ads/ads-create.html"
    model = Ads
    form_class = AdsForm
    success_url = reverse_lazy("ads:ads_list")


class AdsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "ads/ads-edit.html"
    model = Ads
    form_class = AdsForm

    def get_success_url(self):
        return reverse("ads:ads_details", kwargs={"pk": self.object.pk})


class AdsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "ads/ads-delete.html"
    model = Ads
    success_url = reverse_lazy("ads:ads_list")
