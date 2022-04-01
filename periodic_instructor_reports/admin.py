"""
Django admin integration for periodic instructor reports.
"""

from django.contrib import admin
from periodic_instructor_reports.models import (
    PeriodicReportTask,
    PeriodicReportSchedule,
)


@admin.register(PeriodicReportTask)
class PeriodicReportTaskAdmin(admin.ModelAdmin):
    """
    Django admin widget for `PeriodicReportTask`s.
    """

    list_display = ["name", "path", "requires_request"]
    list_filter = ["name", "path", "requires_request"]
    search_fields = ["name", "path"]


@admin.register(PeriodicReportSchedule)
class PeriodicReportScheduleAdmin(admin.ModelAdmin):
    """
    Django admin widget for `PeriodicReportSchedule`s.
    """

    list_display = ["task", "interval", "course_ids", "arguments", "keyword_arguments"]
    list_filter = ["task__name"]
    search_fields = ["task__name", "task__path", "course_ids"]
    raw_id_fields = ("owner",)
