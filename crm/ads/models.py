from django.db import models

from products.models import Product


class Ads(models.Model):
    name = models.CharField(null=False, max_length=150, verbose_name="Название")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name="Рекламируемая услуга",
    )
    channel = models.CharField(max_length=150, verbose_name="Канал продвижения")
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Бюджет (в руб)",
    )

    def __str__(self):
        return "{} ({})".format(self.name, self.product.name)
