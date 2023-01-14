from django.shortcuts import render


def home(request):
    data = {'title': 'Домашняя страница',
            }
    return render(request, 'account/home.html', data)
