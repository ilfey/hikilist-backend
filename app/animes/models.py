from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.TextField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "genres"
        ordering = ["id"]


class Studio(models.Model):
    title = models.TextField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "studios"
        ordering = ["id"]


class Format(models.Model):
    title = models.TextField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "formats"
        ordering = ["id"]


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

    # status = models.GeneratedField(
    #     expression=models.Case(
    #         models.When(
    #             episodes_released__isnull=True,
    #             then=models.Value("Анонсировано"),
    #         ),
    #         models.When(
    #             models.Q(episodes = models.F("episodes_released")),
    #             then=models.Value("Вышло"),
    #         ),
    #         default=models.Value("Выходит"),
    #     ),
    #     output_field=models.CharField(max_length=32),
    #     db_persist=True,
    # )

    @property
    def status(self):
        if self.episodes_released == 0:
            return "Анонсировано"
        elif self.episodes == self.episodes_released:
            return "Вышло"
        elif self.episodes != 0 and self.episodes_released != 0:
            return "Выходит"

    format = models.ForeignKey(Format, on_delete=models.SET_NULL, blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    studios = models.ManyToManyField(Studio, blank=True)
    related = models.ManyToManyField("self", blank=True)

    class Meta:
        db_table = "animes"
        ordering = ["id"]

    def __str__(self):
        return self.title


class List(models.Model):
    title = models.TextField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "lists"
        ordering = ["id"]


class Rate(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, blank=False, null=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, blank=False, null=False)
    list = models.ForeignKey(List, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.user}, {self.anime}"
    
    class Meta:
        db_table = "rates"
        ordering = ["id"]
