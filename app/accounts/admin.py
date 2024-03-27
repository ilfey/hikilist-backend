from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from . import models


class UserResource(resources.ModelResource):
    class Meta:
        model = models.User


@admin.register(models.User)
class UserAdmin(ImportExportModelAdmin):
    model = models.User
    resource_classes = (UserResource,)


@admin.register(models.Rate)
class AdminRate(admin.ModelAdmin):
    model = models.Rate
    list_display = (
        "id",
        "user",
        "anime",
        "list",
        "rating",
    )
    list_filter = (
        "id",
        "user",
        "anime",
        "list",
        "rating",
    )
    save_on_top = True


@admin.register(models.List)
class AdminList(admin.ModelAdmin):
    model = models.List
    list_display = (
        "id",
        "title",
        "user",
        "is_primary",
    )
    search_fields = (
        "id",
        "title",
    )
    list_display_links = ("title",)
    save_on_top = True
