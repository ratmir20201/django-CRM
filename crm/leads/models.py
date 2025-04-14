from django.db import models

from ads.models import Ads


class Lead(models.Model):
    first_name = models.CharField(max_length=100, null=False, verbose_name="Имя")
    last_name = models.CharField(max_length=100, null=False, verbose_name="Фамилия")
    phone = models.CharField(
        max_length=15,
        null=True,
        verbose_name="Номер телефона",
    )
    email = models.EmailField(null=False, verbose_name="Email")
    ad = models.ForeignKey(
        Ads,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Рекламная компания",
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Является ли клиент активным",
    )

    def __str__(self):
        return f"Lead(pk={self.pk}, name={self.last_name} {self.first_name})"
