# future

# standard library


# third-party

# Django
from django.shortcuts import render


# local Django

# Create your views here.
def profile(request):
    return render(request, 'account/profile.html')
