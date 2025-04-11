from rest_framework import serializers

from leads.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "pk", "first_name", "last_name", "phone", "email", "ad"
