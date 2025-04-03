from django import forms

from ads.models import Ads


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = "name", "product", "channel", "budget"
        labels = {
            "name": "Название",
            "product": "Рекламируемая услуга",
            "channel": "Канал продвижения",
            "budget": "Бюджет (в руб)",
        }
