from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ads.models import Ads
from customers.models import Customer
from leads.models import Lead
from products.models import Product


class MainTitleView(LoginRequiredMixin, TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_count"] = Product.objects.count()
        context["advertisements_count"] = Ads.objects.count()
        context["advertisements_count"] = Ads.objects.count()
        context["leads_count"] = Lead.objects.count()
        context["customers_count"] = Customer.objects.count()
        return context
