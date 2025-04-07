from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from leads.forms import LeadForm
from leads.models import Lead


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/leads-create.html"
    model = Lead
    form_class = LeadForm
    success_url = reverse_lazy("leads:leads_list")


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/leads-edit.html"
    model = Lead
    form_class = LeadForm

    def get_success_url(self):
        return reverse(
            "leads:product_detail",
            kwargs={"pk": self.object.pk},
        )


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/leads-delete.html"
    model = Lead
    success_url = reverse_lazy("leads:leads_list")


class LeadsListView(LoginRequiredMixin, ListView):
    template_name = "leads/leads-list.html"
    model = Lead
    context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/leads-detail.html"
    model = Lead
    context_object_name = "object"
