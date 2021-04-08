import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

# Актуальная дата (Сегодняшняя) со временем
now = datetime.datetime.now()


# Модели связанныке с врачами

class Doctor(models.Model):
    specialization = models.CharField(_("Специализация"), max_length=50)
    surname = models.CharField(_("Фамилия"), max_length=50)
    name = models.CharField(_("Имя"), max_length=50)
    last_name = models.CharField(_("Отчество"), max_length=50)
    photo = models.ImageField(_("Фотография врача"))
    description = models.TextField(_("Описание"))
    education = models.TextField(_("Образование"))

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

    def __str__(self):
        return f"{self.surname} {self.name} {self.last_name}"


class RefresherCourse(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="refresher_courses")
    year_of_passage = models.PositiveIntegerField(_("Год прохождения"), validators=[
        MinValueValidator(1900),
        MaxValueValidator(now.year),
    ])
    name_courses = models.TextField(_("Название курса"))

    class Meta:
        verbose_name = "Курсы повышения квалификации"
        verbose_name_plural = "Курсы повышения квалификации"

    def __str__(self):
        return ""


class WorkExperience(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="work_experiences")
    year_of_works = models.PositiveIntegerField(_("Года работы"), validators=[
        MinValueValidator(1900),
        MaxValueValidator(now.year),
    ])
    name_work = models.TextField(_("Работа"))

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

    def __str__(self):
        return ""


class Schedule(models.Model):  # Расписание
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    monday = models.BooleanField(_("Понедельник"))
    tuesday = models.BooleanField(_("Вторник"))
    wednesday = models.BooleanField(_("Среда"))
    thursday = models.BooleanField(_("Четверг"))
    friday = models.BooleanField(_("Пятница"))
    saturday = models.BooleanField(_("Суббота"))
    sunday = models.BooleanField(_("Воскресенье"))


class TimeWork(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    start_work = models.CharField(max_length=5)
    end_work = models.CharField(max_length=5)


class Record(models.Model):
    user_name = models.CharField(_("Имя пациента"), max_length=50)
    user_surname = models.CharField(_("Отчество пациента"), max_length=50)
    user_last_name = models.CharField(_("Фамилия пациента"), max_length=50)
    doctor_name = models.CharField(_("Имя врача"), max_length=50)
    doctor_surname = models.CharField(_("Отчество врача"), max_length=50)
    doctor_last_name = models.CharField(_("Фамилия врача"), max_length=50)
    datetime_record = models.DateTimeField(_("Дата и время приема"))

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
