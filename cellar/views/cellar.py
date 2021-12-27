# future

# standard library


# third-party

# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# local Django

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'cellar/cellar.html')
