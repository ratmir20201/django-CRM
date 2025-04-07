from django.db import models

from ads.models import Ads


class Lead(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Делаем полностью новую модель не расширяющую модель User
    phone = models.CharField(
        max_length=15,
        null=True,
        verbose_name="Номер телефона",
    )
    ad = models.ForeignKey(
        Ads,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Рекламная компания",
    )

    def __str__(self):
        return f"Lead(pk={self.pk}, name={self.user.name})"
