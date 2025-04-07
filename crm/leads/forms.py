from django import forms

from leads.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "user", "phone", "ad"
        labels = {
            "user": "Пользователь",
            "phone": "Описание",
            "ad": "Рекламная компания",
        }
