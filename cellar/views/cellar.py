# future

# standard library


# third-party

# Django
from django.shortcuts import render


# local Django

# Create your views here.


def home(request):
    return render(request, 'cellar/cellar.html')
