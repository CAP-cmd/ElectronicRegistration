import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser

# Актуальная дата (Сегодняшняя) со временем
now = datetime.datetime.now()
# Актуальная дата (Сегодняшняя) без времени, для валидации
today = datetime.date.today()


class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, now.year + 1),
                                                             attrs={"class": "m_birthday"}), label=(_("День рождения")))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"id": "phone_number"}), label=(_("Номер телефона")))
    snils = forms.CharField(widget=forms.TextInput(attrs={"id": "snils"}), label=(_("Снилс")))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("email", "surname", "name", "last_name", "birthday", "phone_number", "snils")

    def clean_birthday(self):
        birthday = self.cleaned_data["birthday"]
        if birthday > today:
            raise ValidationError("Дата рождения не может находится в будущем")
        return birthday


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password")
