# Generated by Django 4.2.4 on 2023-08-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='photos_info')),
            ],
            options={
                'verbose_name': ('Информация',),
                'verbose_name_plural': 'Информации',
            },
        ),
    ]
