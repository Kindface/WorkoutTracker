from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Run(models.Model):
    owner = models.ForeignKey(CustomUser, models.CASCADE, verbose_name="Владелец")
    description = models.TextField(verbose_name="Описание")
    distance = models.FloatField(verbose_name="Дистанция в км", validators=[MinValueValidator(0)])
    time = models.FloatField(verbose_name="Время бега в минутах", validators=[MinValueValidator(0)])
    date = models.DateField(default=timezone.now, verbose_name="Дата бега")

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse('runs')