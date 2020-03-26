from django.db import models
from accounts.models import CustomUser
from django.core.validators import MinValueValidator


class Exercise(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование упражнения")
    sets = models.IntegerField(verbose_name="Подходы", validators=[MinValueValidator(0)])
    reps = models.IntegerField(verbose_name="Повторения", validators=[MinValueValidator(0)])
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return '{} Подходов:{} Повторений:{}'.format(self.name, self.sets, self.reps)
