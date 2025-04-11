from rest_framework import serializers

from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "pk", "name", "product", "document", "start_date", "end_date", "cost"
