from django import forms

from leads.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "first_name", "last_name", "phone", "email", "ad"
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "phone": "Номер телефона",
            "email": "Email",
            "ad": "Рекламная компания",
        }
