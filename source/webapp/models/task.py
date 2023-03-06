from django.db import models

import webapp.models


# Create your models here.


class Task(models.Model):
    title = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    status = models.ForeignKey(
        to='webapp.Status',
        related_name='statuses',
        on_delete=models.PROTECT,
        verbose_name='Статус'
    )
    type = models.ManyToManyField(
        to='webapp.Type',
        related_name='types',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
        null=True
    )

    def __str__(self):
        return f'{self.title} | {self.description} - {self.created_at}'
