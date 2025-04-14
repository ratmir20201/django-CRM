from django import forms

from customers.models import Customer
from leads.models import Lead


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "lead", "contract"
        labels = {
            "lead": "Потенциальный клиент",
            "contract": "Контракт",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        used_leads = Customer.objects.values_list("lead_id", flat=True)
        self.fields["lead"].queryset = Lead.objects.exclude(id__in=used_leads)
