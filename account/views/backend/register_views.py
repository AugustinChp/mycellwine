# future

# standard library


# third-party

# Django
from django.shortcuts import render


def register(request):
    return render(request, "account/register.html")
