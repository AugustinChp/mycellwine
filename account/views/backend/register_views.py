# future

# standard library
import json
import pdb
from datetime import datetime

# third-party
from validate_email import validate_email

# Django
from django.views import View
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.translation import activate, gettext as _
from django.conf import settings
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

# Django local
from account.models import User
from account.utils import account_activation_token


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            error_message = _(
                'username should only contain alphanumeric characters')
            return JsonResponse({'username_error': error_message}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': _('sorry username in use, choose another one')}, status=409)
        return JsonResponse({'username_valid': True})


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is not valid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use, choose another one'}, status=409)
        return JsonResponse({'email_valid': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, "account/register.html")

    def post(self, request):

        # Get user data
        username_field = request.POST['username']
        email_field = request.POST['email']
        birth_year_field = request.POST['birth_year']
        password_field = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        # Validate
        if not User.objects.filter(username=username_field).exists():
            if not User.objects.filter(email=email_field).exists():
                if not birth_year_field.isnumeric():
                    messages.error(request, 'Birth year must be a number')
                    return render(request, "account/register.html", context)
                if (int(datetime.now().year)-int(birth_year_field)) < 18:
                    messages.error(
                        request, 'You are not old enough to create an account')
                    return render(request, "account/register.html", context)
                if len(password_field) < 6:
                    messages.error(request, 'Password is too short')
                    return render(request, "account/register.html", context)

                user = User.objects.create_user(
                    username=username_field,
                    email=email_field,
                    birth_year=birth_year_field,
                    password=password_field)

                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

                domain = get_current_site(request).domain
                link = reverse('activate', kwargs={
                               'uidb64': uidb64, 'token': account_activation_token.make_token(user)})
                activate_url = "http://"+domain+link
                email_subject = "Activate your account"
                email_body = 'Hi ' + user.username + \
                    ', Please the link below to activate your account \n' + activate_url
                email = EmailMessage(
                    email_subject,
                    email_body,
                    settings.EMAIL_HOST_USER,
                    [email_field],
                )
                email.send(fail_silently=False)
                messages.success(
                    request, f'Welcome {user.username} ! Your account has been successfully created !')
                return render(request, "account/register.html")

        # Create user account

        return render(request, "account/register.html")
