from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import PupilForm, CoursForm
from django.views.generic import DetailView
from .models import Pupil, Cours
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('account')
            except IntegrityError:
                return render(request, 'account/signup.html',
                              {'form': UserCreationForm(),
                               'error': 'Это имя пользователя уже используется!'})
        else:
            return render(request, 'account/signup.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'account/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'account/login.html', {'form': AuthenticationForm(),
                                                          'error': 'Неверный логин или пароль'})
        else:
            login(request, user)
            return redirect('account')


def home(request):
    return redirect('login')


def account(request):
    pupils = Pupil.objects.filter(teacher=request.user)
    courses = Cours.objects.filter(author=request.user)
    return render(request, 'account/account.html', {'pupils': pupils, 'courses': courses})


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
            pupil = form.save(commit=False)
            pupil.teacher = request.user
            pupil.save()
            return redirect('account')
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
            cours = form.save(commit=False)
            cours.author = request.user
            cours.save()
            return redirect('account')
        else:
            error = 'Форма не верная'

    form = CoursForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'account/addcours.html', data)
