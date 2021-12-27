# future

# standard library


# third-party

# Django
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt


# local Django
from .views import *

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name="validate-email"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),
    path('reset-password/', ResetPasswordView.as_view(), name="reset-password"),
    path('set-new-password/<uidb64>/<token>',
         CompletePasswordReset.as_view(), name="set-new-password"),
]
