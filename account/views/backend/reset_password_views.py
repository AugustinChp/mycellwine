# standard library
import pdb

from validate_email import validate_email

# Django
from django.views import View
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

# Django local
from account.models import User
from helpers.email_threading import EmailThread


class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'account/reset-password.html')

    def post(self, request):
        email_field = request.POST['email']

        context = {
            'values': request.POST
        }

        if not validate_email(email_field):
            messages.error(request, 'Please supply a valid email')
            return render(request, 'account/reset-password.html', context)

        domain = get_current_site(request).domain

        user = User.objects.filter(email=email_field)

        if user.exists():
            email_contents = {
                'user': user[0],
                'domain': domain,
                'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token': PasswordResetTokenGenerator().make_token(user[0])
            }

            link = reverse('set-new-password', kwargs={
                'uidb64': email_contents['uid'], 'token': email_contents['token']})

            reset_url = "http://"+email_contents['domain']+link
            email_subject = "Password reset instructions"
            email_body = 'Hi ' + user[0].username + \
                ', Please the link below to reset your password \n' + reset_url
            email = EmailMessage(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [email_field],
            )
            EmailThread(email).start()
            messages.success(
                request, f'Welcome {user[0].username} ! Your account has been successfully created !')
            return redirect('login')

        messages.error(
            request, f"You don't account with this email.")

        return render(request, 'account/reset-password.html')


class CompletePasswordReset(View):
    def get(self, request, uidb64, token):

        context = {
            'uidb64': uidb64,
            'token': token,
        }

        return render(request, 'account/set-new-password.html', context)

    def post(self, request, uidb64, token):

        context = {
            'uidb64': uidb64,
            'token': token,
        }

        password_field = request.POST['password']

        if len(password_field) < 6:
            messages.error(request, 'Password too short')
            return render(request, 'account/set-new-password.html', context)

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            user.set_password(password_field)
            user.save()

            messages.success(request, 'Passord reset successfully')

        except Exception as ex:
            messages.info(request, 'Something went wrong, try again')
            return render(request, 'account/set-new-password.html', context)

        return redirect('login')
