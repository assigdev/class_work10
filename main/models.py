from django.db import models


class Test(models.Model):
    name = models.CharField('Имя', max_length=100)
    age = models.SmallIntegerField('Возраст')
    birth = models.DateField('ДР', blank=True, null=True)
