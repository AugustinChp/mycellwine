# future

# standard library


# third-party

# Django
from django.urls import include, path


# local Django
from .views import cellar


urlpatterns = [
    path('', cellar.home),
]
