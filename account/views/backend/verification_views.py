# standard library
import json
import pdb
from datetime import datetime

# third-party
from validate_email import validate_email

# Django
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

# Django local
from account.models import User
from account.utils import account_activation_token


class VerificationView(View):
    def get(self, request, uidb64, token):

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                messages.error(request, 'User is already activate')
                return redirect('login')
            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.email_verified = True
            user.save()

            messages.success(request, 'Account activate successfully')
            return redirect('login')
        except Exception as ex:
            pass

        return redirect('login')
