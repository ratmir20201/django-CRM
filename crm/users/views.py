from django.views.generic import TemplateView

from ads.models import Ads
from products.models import Product


class MainTitleView(TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_count"] = Product.objects.count()
        context["advertisements_count"] = Ads.objects.count()
        return context
