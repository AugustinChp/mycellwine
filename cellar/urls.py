# future

# standard library


# third-party

# Django
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# local Django
from .views import *


urlpatterns = [
    path('', login_required(CellarView.as_view(), login_url='login'), name='cellar'),
    path('add-cellar/', login_required(AddCellarView.as_view(),
         login_url='login'), name="add-cellar"),
    path('edit-cellar/', login_required(EditCellarView.as_view(),
         login_url='login'), name="edit-cellar"),
    path('delete-cellar/', login_required(DeleteCellarView.as_view(),
         login_url='login'), name="delete-cellar"),
]
