from django.db import models
from django.db.models.base import ModelState


class Article(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=70)
    username = models.CharField('Псевдоним', max_length=50)
    city = models.CharField('Город', max_length=70)
    state = models.CharField('Штат', max_length=50)
    zip = models.CharField('Zip-code', max_length=50)
    comment = models.TextField('Комментарий')
    date = models.DateTimeField('Дата комментария')

    def __str__(self):
        return f'{self.date}'
