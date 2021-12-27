# standard library

# Django
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import auth, messages

# Django local


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        return redirect('login')
