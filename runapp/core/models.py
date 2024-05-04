from django.contrib.auth.models import User
from django.db import models


class Teams(models.Model):
    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = "команды"

    rangeteam = range(100, 236)
    TEAM = [(i, i) for i in rangeteam]

    team = models.PositiveIntegerField(verbose_name='команда', unique=True, choices=TEAM, default=100)

    def __str__(self):
        return str(self.team)


class Runner(models.Model):
    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = "участники"

    USERNAME_FIELD = 'user'

    GENDER = [
        ('м', "м"), ("ж", "ж")
    ]
    CATEGORY = [
        (1, 'Новичок - 50 км'), (2, 'Легкий - 100 км'), (3, 'Средний - 200 км'), (4, 'Тяжелый - 400 км'),
        (5, 'Ультра - 900 км')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Номер участника', db_index=True)
    nickname= models.CharField(max_length=12, verbose_name='никнейм',null=True)
    runner_team = models.ForeignKey(Teams, on_delete=models.DO_NOTHING, verbose_name='команда', db_index=True)
    runner_age = models.PositiveIntegerField(verbose_name='возраст', db_index=True)
    runner_category = models.PositiveIntegerField(verbose_name='Заявляетесь в группу', choices=CATEGORY, default=1,
                                                  db_index=True)
    runner_gender = models.CharField(max_length=1, choices=GENDER, verbose_name='пол участника', default='м')
    zabeg22 = models.BooleanField(verbose_name='Участник МыZaБег 2022', default=False)
    zabeg23 = models.BooleanField(verbose_name='Участник МыZaБег 2023', default=False)
    # category_updated = models.PositiveIntegerField(verbose_name='Начальная группа', choices=CATEGORY, blank=True,
    #                                                null=True)
    # completed = models.BooleanField(default=False, verbose_name="Выполнена квал-я", )

    def __str__(self):
        return str(self.user)
