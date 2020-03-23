from django.db import models
from accounts.models import CustomUser
from django.utils import timezone


class Run(models.Model):
    owner = models.ForeignKey(CustomUser, models.CASCADE, verbose_name="Владелец")
    description = models.TextField(verbose_name="Описание")
    distance = models.FloatField(verbose_name="Дистанция в км")
    time = models.FloatField(verbose_name="Время бега в минутах")
    date = models.DateField(default=timezone.now, verbose_name="Дата бега")

    def __str__(self):
        return str(self.date)
