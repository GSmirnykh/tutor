from django.db import models


class Cours(models.Model):
    title = models.CharField('Название курса', max_length=50)
    description = models.TextField('Описание курса')
    lenght = models.IntegerField('Продолжительность курса')
    cost_individual = models.IntegerField('Стоимость индивидульного занятия')
    cost_group = models.IntegerField('Стоимость группового занятия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Pupil(models.Model):
    CHOISES = [
        ('individual', 'индивидуальное'),
        ('group', 'групповое')
    ]
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    parents = models.TextField('Представитель')
    phone = models.CharField('Контактный телефон', max_length=10)
    education_form = models.CharField('Форма обучения', max_length=50, choices=CHOISES, default='individual')


    def __str__(self):
        pupil = self.name + ' ' + self.surname
        return pupil

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
