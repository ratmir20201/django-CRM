from django.db import models

from contracts.models import Contract
from leads.models import Lead


class Customer(models.Model):
    lead = models.OneToOneField(
        Lead,
        on_delete=models.CASCADE,
        verbose_name="Потенциальный клиент",
        related_name="active_client",
    )
    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        verbose_name="Контракт",
        related_name="active_client",
    )

    def __str__(self):
        return f"{self.lead.last_name} {self.lead.first_name} — активный клиент"
