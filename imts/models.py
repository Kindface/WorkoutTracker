from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from accounts.models import CustomUser
from django.utils import timezone


class IMT(models.Model):
    owner = models.ForeignKey(CustomUser, models.CASCADE, verbose_name="Владелец")
    date = models.DateField(default=timezone.now, verbose_name="Дата замера")
    height = models.FloatField(verbose_name="Рост в см", validators=[MinValueValidator(0)])
    weight = models.FloatField(verbose_name="Вес в кг", validators=[MinValueValidator(0)])
    imt = models.FloatField(verbose_name="Индекс массы тела", validators=[MinValueValidator(1)])
    result = models.CharField(verbose_name="Результат", max_length=255)


