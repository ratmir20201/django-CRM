from django.db import models


class Product(models.Model):
    name = models.CharField(null=False, max_length=150)
    description = models.TextField(blank=True, null=False, default="", max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Product(pk={}, name={!r}".format(self.pk, self.name)
