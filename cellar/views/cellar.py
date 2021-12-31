# future

# standard library
import pdb

# third-party

# Django
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator


# local Django
from cellar.models import Cellar

# Create your views here.


class CellarView(View):
    def get(self, request):
        current_user = request.user
        if not current_user.has_cellars:
            return redirect('add-cellar')
        cellar = current_user.cellars.first()
        bottles = cellar.cellarbottle_set.all()
        paginator = Paginator(bottles, 5)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)

        context = {
            'bottles': bottles,
            'page_obj': page_obj
        }

        return render(request, 'cellar/cellar.html', context)


class AddCellarView(View):
    def get(self, request):
        current_user = request.user
        if current_user.has_cellars:
            return redirect('cellar')
        return render(request, 'cellar/add-cellar.html')

    def post(self, request):
        current_user = request.user
        invite_code = request.POST.get('invite_code')

        context = {
            'values': request.POST
        }

        if current_user.has_cellars:
            return redirect('cellar')

        if invite_code:
            try:
                cellar = Cellar.objects.filter(pk=invite_code).first()
                if cellar.exists():
                    current_user.cellars.add(cellar)
                    return redirect('cellar')
                messages.error(request, 'Incorrect invitation code')
                return redirect(request, 'cellar/add-cellar.html', context)

            except Exception as ex:
                messages.error(request, 'Incorrect invitation code')
                return render(request, 'cellar/add-cellar.html', context)

        if not invite_code:
            cellar = Cellar.objects.create(
                created_by=current_user, modified_by=current_user)
            current_user.cellars.add(cellar)
            return redirect('cellar')
        return render(request, 'cellar/add-cellar.html')


class EditCellarView(View):
    def get(self, request):
        current_user = request.user
        if not current_user.has_cellars:
            return redirect('add-cellar')
        return render(request, 'cellar/edit-cellar.html')


class DeleteCellarView(View):
    def post(self, request):
        current_user = request.user
        cellar = current_user.cellars.first()
        if cellar.created_by == current_user:
            cellar.delete()
            return redirect('cellar')

        return render(request, 'cellar/edit-cellar.html')
