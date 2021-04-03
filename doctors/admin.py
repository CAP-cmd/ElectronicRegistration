from django.contrib import admin

from . import models


class RefresherCourseInline(admin.TabularInline):
    model = models.RefresherCourse


class WorkExperienceInline(admin.TabularInline):
    model = models.WorkExperience


class ScheduleInline(admin.TabularInline):
    extra = 1
    model = models.Schedule


class DoctorAdmin(admin.ModelAdmin):
    inlines = [
        RefresherCourseInline,
        WorkExperienceInline,
        ScheduleInline,
    ]


admin.site.register(models.Doctor, DoctorAdmin)
