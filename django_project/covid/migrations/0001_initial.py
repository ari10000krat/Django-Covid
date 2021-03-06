# Generated by Django 3.2 on 2021-04-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=70, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=50, verbose_name='Псевдоним')),
                ('city', models.CharField(max_length=70, verbose_name='Город')),
                ('state', models.CharField(max_length=50, verbose_name='Штат')),
                ('zip', models.CharField(max_length=50, verbose_name='Zip-code')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateTimeField(verbose_name='Дата комментария')),
            ],
        ),
    ]
