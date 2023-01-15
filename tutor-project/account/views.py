from django.shortcuts import render, redirect
from .forms import PupilForm

def home(request):
    data = {'title': 'Домашняя страница',
            }
    return render(request, 'account/home.html', data)

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
