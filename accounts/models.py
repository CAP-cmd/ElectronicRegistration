from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("Электронная почта"), unique=True)
    surname = models.CharField(_("Фамилия"), max_length=50)
    name = models.CharField(_("Имя"), max_length=50)
    last_name = models.CharField(_("Отчество"), max_length=50)
    birthday = models.DateField(_("День Рождения"))
    phone_number = models.CharField(_("Номер телефона"), max_length=18, unique=True)
    snils = models.CharField(_("СНИЛС"), max_length=14, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "surname",
        "name",
        "last_name",
        "birthday",
        "phone_number",
        "snils"
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
