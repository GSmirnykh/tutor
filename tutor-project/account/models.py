from django.db import models
from django.contrib.auth.models import User


class Cours(models.Model):
    course_id = models.AutoField
    title = models.CharField('Название курса', max_length=50)
    description = models.TextField('Описание курса')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    lenght = models.IntegerField('Продолжительность курса, часов', null=True)
    cost_individual = models.IntegerField('Стоимость индивидульного занятия', null=True, blank=True)
    cost_group = models.IntegerField('Стоимость группового занятия', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Pupil(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOISES = [
        ('individual', 'индивидуальное'),
        ('group', 'групповое')
    ]
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    age = models.IntegerField('Возраст', null=True)
    parents = models.TextField('Представитель')
    phone = models.IntegerField('Контактный телефон')
    education_form = models.CharField('Форма обучения', max_length=50, choices=CHOISES, default='individual')
    course = models.ForeignKey(Cours, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        pupil = f'{self.name} {self.surname} - {self.course.title}'
        return pupil

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
