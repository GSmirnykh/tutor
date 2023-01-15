from .models import Pupil, Cours
from django.forms import ModelForm, TextInput, Textarea, Select

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
            'age': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            'parents': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Представитель'
            }),
            'phone': TextInput(attrs={
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