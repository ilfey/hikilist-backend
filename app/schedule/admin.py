from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Schedule)
class AdminSchedule(admin.ModelAdmin):
    model = models.Schedule
    list_display=("id", "anime", "episode", "date",)
    search_fields=("id", "anime__pk", "anime", "date",)
    list_display_links = ("anime",)
    list_filter = ("date",)
    save_on_top = True