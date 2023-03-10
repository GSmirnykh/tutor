from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView

from .forms import CoursForm, PupilForm
from .models import Cours, Pupil


def home(request):
    return render(request, "account/home.html")


def signup(request):
    if request.method == "GET":
        return render(request, "account/signup.html", {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect("account")
            except IntegrityError:
                return render(
                    request,
                    "account/signup.html",
                    {
                        "form": UserCreationForm(),
                        "error": "Это имя пользователя уже используется!",
                    },
                )
        else:
            return render(
                request,
                "account/signup.html",
                {"form": UserCreationForm(), "error": "Пароли не совпадают"},
            )


def loginuser(request):
    if request.method == "GET":
        return render(request, "account/login.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "account/login.html",
                {"form": AuthenticationForm(), "error": "Неверный логин или пароль"},
            )
        else:
            login(request, user)
            return redirect("account")


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")


def account(request):
    pupils = Pupil.objects.filter(teacher=request.user)
    courses = Cours.objects.filter(author=request.user)
    return render(
        request, "account/account.html", {"pupils": pupils, "courses": courses}
    )


class PupilDetailView(DetailView):
    model = Pupil
    template_name = "account/pupilview.html"
    context_object_name = "pupil"


class CoursDetailView(DetailView):
    model = Cours
    template_name = "account/coursview.html"
    context_object_name = "cours"


def add_pupil(request):
    error = ""
    if request.method == "POST":
        form = PupilForm(request.POST)
        if form.is_valid():
            pupil = form.save(commit=False)
            pupil.teacher = request.user
            pupil.save()
            return redirect("account")
        else:
            error = "Форма не верная"

    form = PupilForm()
    data = {"form": form, "error": error}
    return render(request, "account/addpupil.html", data)


def add_cours(request):
    error = ""
    if request.method == "POST":
        form = CoursForm(request.POST)
        if form.is_valid():
            cours = form.save(commit=False)
            cours.author = request.user
            cours.save()
            return redirect("account")
        else:
            error = "Форма не верная"

    form = CoursForm()
    data = {"form": form, "error": error}
    return render(request, "account/addcours.html", data)


def edit_cours(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == "POST":
        form = CoursForm(data=request.POST, instance=cours)
        if form.is_valid():
            cours = form.save(commit=False)
            cours.author = request.user
            cours.save()
            return redirect("cours_detail", pk=cours.pk)
    else:
        form = CoursForm(instance=cours)
    context = {"form": form}
    return render(request, "account/editcours.html", context)


def edit_pupil(request, pk):
    pupil = get_object_or_404(Pupil, pk=pk)
    if request.method == "POST":
        form = PupilForm(data=request.POST, instance=pupil)
        if form.is_valid():
            pupil = form.save(commit=False)
            pupil.teacher = request.user
            pupil.save()
            return redirect("pupil_detail", pk=pupil.pk)
    else:
        form = PupilForm(instance=pupil)
    context = {"form": form}
    return render(request, "account/editpupil.html", context)
