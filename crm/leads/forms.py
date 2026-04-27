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

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name:
            exists = Lead.objects.filter(
                first_name=first_name,
                last_name=last_name
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "Лид с таким именем и фамилией уже существует"
                )

        return cleaned_data
