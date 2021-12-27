# standard library

# Django
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import auth, messages

# Django local


class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):

        email_field = request.POST["email"]
        password_field = request.POST["password"]

        if email_field and password_field:
            user = auth.authenticate(
                email=email_field, password=password_field)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('cellar')

                messages.error(
                    request, 'Account is not active, please check your email')
                return render(request, 'account/login.html')
            messages.error(
                request, 'Invalid credentials, try again')
            return render(request, 'account/login.html')
        messages.error(
            request, 'Please fill all fields')
        return render(request, 'account/login.html')
