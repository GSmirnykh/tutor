from django.db import models


class Cours(models.Model):
    title = models.CharField('Название курса', max_length=50)
    description = models.TextField('Описание курса')
    lenght = models.IntegerField('Продолжительность курса',)
    cost_individual = models.IntegerField('Стоимость индивидульного занятия')
    cost_group = models.IntegerField('Стоимость группового занятия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Pupil(models.Model):
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    parents = models.TextField('Представитель')
    phone = models.CharField('Контактный телефон', max_length=10)
    is_group = models.BooleanField('Групповые занятия', default=False)
    is_individual = models.BooleanField('Индивидуальные занятия', default=False)

    def __str__(self):
        pupil = self.name + ' ' + self.surname
        return pupil

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
