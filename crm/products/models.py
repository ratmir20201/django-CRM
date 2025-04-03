from django.db import models


class Product(models.Model):
    name = models.CharField(null=False, max_length=150, verbose_name="Название")
    description = models.TextField(
        blank=True,
        null=False,
        default="",
        max_length=500,
        verbose_name="Описание",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена (в руб)",
    )

    def __str__(self):
        return "Product(pk={}, {!r} - {}руб)".format(
            self.pk,
            self.name,
            self.price,
        )
