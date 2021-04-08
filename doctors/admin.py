from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class RefresherCourseInline(admin.TabularInline):
    extra = 1
    model = models.RefresherCourse


class WorkExperienceInline(admin.TabularInline):
    extra = 1
    model = models.WorkExperience


class ScheduleInline(admin.TabularInline):
    max_num = 1
    model = models.Schedule


class TimeWorkInline(admin.TabularInline):
    extra = 1
    model = models.TimeWork


class DoctorAdmin(admin.ModelAdmin):
    fields = ["specialization", "surname", "name", "last_name", "photo", "preview", "description", "education"]
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f"<img src='{obj.photo.url}'>")

    preview.short_description = "Предварительный просмотр"

    inlines = [
        RefresherCourseInline,
        WorkExperienceInline,
        ScheduleInline,
        TimeWorkInline,
    ]


# class RecordAdmin(admin.ModelAdmin):


admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Record)
