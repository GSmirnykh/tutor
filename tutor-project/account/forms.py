from django.forms import ModelForm, NumberInput, Select, Textarea, TextInput

from .models import Cours, Pupil


class PupilForm(ModelForm):
    class Meta:
        model = Pupil
        fields = ['name', 'surname', 'age', 'parents', 'phone', 'education_form', 'course']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'age': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            'parents': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Представитель'
            }),
            'phone': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            'education_form': Select(attrs={
                'individual': 'Индивидуальное',
                'group': 'Групповое'
            }),
            'course': Select(attrs={
                Cours.course_id: Cours.title,
            })
        }


class CoursForm(ModelForm):
    class Meta:
        model = Cours
        fields = ['title', 'description', 'lenght', 'cost_individual', 'cost_group']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание курса'
            }),
            'lenght': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Продолжительность курса'
            }),
            'cost_individual': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость индивидуального занятия'
            }),
            'cost_group': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость группового занятия'
            }),
        }
