from django.contrib import admin

from . import models


# Register your models here.

admin.site.register(models.Genre)
admin.site.register(models.Studio)
admin.site.register(models.Format)
admin.site.register(models.Anime)
admin.site.register(models.List)
admin.site.register(models.AnimeUserRate)