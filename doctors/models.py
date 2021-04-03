import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

# Актуальная дата (Сегодняшняя) со временем
now = datetime.datetime.now()


class Doctor(models.Model):
    specialization = models.CharField(_("Специализация"), max_length=50)
    surname = models.CharField(_("Фамилия"), max_length=50)
    name = models.CharField(_("Имя"), max_length=50)
    last_name = models.CharField(_("Отчество"), max_length=50)
    photo = models.ImageField(_("Фотография врача"))
    description = models.TextField(_("Описание"))
    education = models.CharField(_("Образование"), max_length=50)

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

    def __str__(self):
        return f"{self.surname} {self.name} {self.last_name}"


class RefresherCourse(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    year_of_passage = models.PositiveIntegerField(_("Год прохождения"), validators=[
        MinValueValidator(1900),
        MaxValueValidator(now.year),
    ])
    name_courses = models.CharField(_("Название курса"), max_length=75)

    class Meta:
        verbose_name = "Курсы повышения квалификации"
        verbose_name_plural = "Курсы повышения квалификации"

    def __str__(self):
        return ""


class WorkExperience(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    year_of_works = models.PositiveIntegerField(_("Года работы"), validators=[
        MinValueValidator(1900),
        MaxValueValidator(now.year),
    ])

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

    def __str__(self):
        return ""


class Schedule(models.Model):  # Расписание
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()