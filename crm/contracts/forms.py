from django import forms

from contracts.models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = "name", "product", "document", "start_date", "end_date", "cost"
        labels = {
            "name": "Название",
            "product": "Рекламируемая услуга",
            "document": "Файл с документом",
            "start_date": "Дата заключения контракта",
            "end_date": "Контракт действует до",
            "cost": "Сумма (в руб)",
        }
