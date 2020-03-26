from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from exercises.models import Exercise


class Workout(models.Model):
    date = models.DateField(default=timezone.now, verbose_name="Дата тренировки")
    description = models.TextField(verbose_name="Описание")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Владелец")
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return str(self.date)


