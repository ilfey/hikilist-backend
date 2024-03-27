from django.contrib import admin

from . import models


# Register your models here.


@admin.register(models.Genre)
class AdminGenre(admin.ModelAdmin):
    model = models.Genre
    list_display = (
        "id",
        "title",
    )
    search_fields = (
        "id",
        "title",
    )
    list_display_links = ("title",)
    save_on_top = True


@admin.register(models.Studio)
class AdminStudio(admin.ModelAdmin):
    model = models.Studio
    list_display = (
        "id",
        "title",
    )
    search_fields = (
        "id",
        "title",
    )
    list_display_links = ("title",)
    save_on_top = True


@admin.register(models.Format)
class AdminFormat(admin.ModelAdmin):
    model = models.Format
    search_fields = (
        "id",
        "title",
    )
    list_display = (
        "id",
        "title",
    )
    list_display_links = ("title",)
    save_on_top = True


@admin.register(models.Anime)
class AdminAnime(admin.ModelAdmin):
    model = models.Anime
    list_display = (
        "id",
        "title",
        "episodes",
        "episodes_released",
        "format",
        "status",
        "announcement",
        "started",
        "released",
    )
    search_fields = (
        "id",
        "title",
        "episodes",
        "episodes_released",
        "announcement",
        "started",
        "released",
    )
    list_filter = (
        "episodes",
        "format",
        "episodes_released",
        "announcement",
        "started",
        "released",
    )
    list_editable = (
        "episodes",
        "episodes_released",
    )
    list_display_links = ("title",)
    save_on_top = True
