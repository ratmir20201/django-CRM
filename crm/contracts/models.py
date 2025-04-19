import os

from django.db import models
from django.utils import timezone

from products.models import Product


class Contract(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="Название")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        verbose_name="Предоставляемая услуга",
    )
    document = models.FileField(
        null=False,
        upload_to="contracts/documents/",
        verbose_name="Файл с документом",
    )
    start_date = models.DateField(
        null=False,
        default=timezone.now,
        verbose_name="Дата заключения контракта",
    )
    end_date = models.DateField(null=False, verbose_name="Контракт действует до")
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма (в руб)",
    )
    is_signed = models.BooleanField(
        default=False,
        verbose_name="Является ли контракт подписанным",
    )

    def delete(self, *args, **kwargs):
        """Удаляет файл с диска перед удалением объекта."""
        if self.document and os.path.isfile(self.document.path):
            os.remove(self.document.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return (
            f"Contract(name={self.name}, product={self.product.name}, summ={self.cost})"
        )
