from django.shortcuts import render, redirect
from .forms import PupilForm, CoursForm
from django.views.generic import DetailView
from .models import Pupil, Cours


def home(request):
    data = {'title': 'Домашняя страница',
            }
    return render(request, 'account/home.html', data)


class PupilDetailView(DetailView):
    model = Pupil
    template_name = 'account/pupilview.html'
    context_object_name = 'pupil'


class CoursDetailView(DetailView):
    model = Cours
    template_name = 'account/coursview.html'
    context_object_name = 'cours'


def add_pupil(request):
    error = ''
    if request.method == 'POST':
        form = PupilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верная'

    form = PupilForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'account/addpupil.html', data)


def add_cours(request):
    error = ''
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верная'

    form = CoursForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'account/addcours.html', data)
