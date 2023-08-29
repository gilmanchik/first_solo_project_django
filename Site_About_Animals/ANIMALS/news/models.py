from django.db import models


class Articles(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='Название'
    )

    anons = models.CharField(
        max_length=128,
        verbose_name='Анонс'
    )

    text = models.TextField(
        verbose_name='Текст статьи'
    )

    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость',
        verbose_name_plural = 'Новости'