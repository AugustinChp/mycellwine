# future

# standard library

# third-party

# Django
from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin, UserManager, AbstractBaseUser
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# local Django
from account.models import Profile
from cellar.models import Cellar


class MyUserManager(UserManager):
    def _create_user(self, username, email, birth_year, password, ** extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        if not birth_year:
            raise ValueError('The given birth year must be set')
        if (int(timezone.now().year)-int(birth_year)) < 18:
            raise ValueError('You must be a legacy adult')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.birth_year = birth_year
        user.save(using=self._db)
        profile = Profile.objects.create(
            user=user, created_by=user, modified_by=user)
        profile.save(using=self._db)
        return user

    def create_user(self, username, email, birth_year, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(username, email, birth_year, password, **extra_fields)

    def create_superuser(self, username, email, birth_year, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'CREATOR')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, birth_year, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=False, unique=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES,
                            default='SUBSCRIBER', blank=True)
    birth_year = models.IntegerField(default=1900)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    cellars = models.ManyToManyField(Cellar)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    email_verified = models.BooleanField(
        _('email_verified'),
        default=False,
        help_text=_(
            'Designates whether this user email is verified. '
        ),
    )
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'birth_year']

    @property
    def has_cellars(self):
        return self.cellars.exists()
