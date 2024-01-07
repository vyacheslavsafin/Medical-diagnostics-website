from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
        ordering = ('name',)


class Service(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена')
    duration = models.IntegerField(verbose_name='Продолжительность')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Направление')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ('name', 'category',)


class Appointment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Направление', **NULLABLE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    date = models.DateTimeField(verbose_name='Дата приёма')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.service} ({self.date})'

    class Meta:
        verbose_name = 'Приём'
