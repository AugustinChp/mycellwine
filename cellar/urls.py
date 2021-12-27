# future

# standard library


# third-party

# Django
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt


# local Django
from .views import cellar


urlpatterns = [
    path('', cellar.home, name='cellar'),
]
