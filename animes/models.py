from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.TextField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.title


class Studio(models.Model):
    title = models.TextField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.title


class Format(models.Model):
    title = models.TextField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.title


class Anime(models.Model):
    malId = models.PositiveBigIntegerField(blank=True, null=True)

    title = models.TextField(max_length=1000, blank=False, null=False)
    poster = models.ImageField(upload_to="posters", blank=True, null=True)
    description = models.TextField(max_length=10000, blank=True, null=True)

    episodes = models.PositiveIntegerField(blank=True, null=True)
    episodes_released = models.PositiveIntegerField(blank=True, null=True)

    announcement = models.DateField(blank=True, null=True)
    started = models.DateField(blank=True, null=True)
    released = models.DateField(blank=True, null=True)

    format = models.ForeignKey(Format, on_delete=models.SET_NULL, blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    studios = models.ManyToManyField(Studio, blank=True)
    related = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.title


class List(models.Model):
    title = models.TextField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.title


class AnimeUserRate(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, blank=False, null=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, blank=False, null=False)
    list = models.OneToOneField(List, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.user}, {self.anime}"
