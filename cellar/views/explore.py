# future

# standard library
import pdb

# third-party

# Django
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


# local Django
from cellar.models import Bottle
from account.models import User

# Create your views here.


class ExploreView(View):
    def get(self, request):
        admin = User.objects.filter(role='CREATOR')
        bottles = Bottle.objects.filter(
            Q(created_by__in=admin) | Q(modified_by__in=admin))
        paginator = Paginator(bottles, 5)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)

        context = {
            'bottles': bottles,
            'page_obj': page_obj
        }
        return render(request, 'cellar/cellar.html', context)
