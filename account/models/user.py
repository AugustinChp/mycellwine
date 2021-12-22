# future

# standard library
from datetime import datetime

# third-party

# Django
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, birth_year, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.birth_year = birth_year
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, birth_year, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )

        user.birth_year = birth_year
        user.staff = True
        user.admin = True
        user.confirmed = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=225,
        unique=True,
    )
    birth_year = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    confirmed_date = models.DateTimeField(blank=True, null=True)

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'  # Email & Password are required by default.
    REQUIRED_FIELDS = ['birth_year']

    objects = UserManager()

    class Meta:
        db_table = 'User'
        app_label = 'account'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_confirmed(self):
        "Is the user confirmed account ?"
        return self.confirm
