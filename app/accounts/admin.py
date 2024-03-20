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