from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Creates a new Customer. Emails and Phone Numbers are unique identifiers. Email and Password are used to log
        in customers
        """
        if not email:
            raise ValueError(_("A valid email is required"))

        email = self.normalize_email(email)
        user = self.model(
            email=email, **extra_fields
        )  # extra fields caters for fields like is_active
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates a superuser who basically have all rights and permissions to do anything and access everything in the
        system
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff option as True"))
        elif extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser option as True"))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    account_type = models.CharField(max_length=10, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    id_number = models.CharField(max_length=8, null=False, blank=False, unique=True)
    mobile_number = models.CharField(max_length=13, null=True, blank=True)
    active = models.BooleanField(null=False, blank=False, default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["id_number", "gender", "account_type"]

    objects = AccountManager()

    def __str__(self):
        return self.email
