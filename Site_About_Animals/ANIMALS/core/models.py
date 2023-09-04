from django.db import models


class Information(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Заголовок'
    )

    description = models.TextField(
        verbose_name='Описание'
    )

    def get_absolute_url(self):
        return f'/{self.id}'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация',
        verbose_name_plural = 'Информации'
