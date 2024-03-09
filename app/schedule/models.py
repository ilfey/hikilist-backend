from django.db import models

# Create your models here.
class Schedule(models.Model):
    anime = models.ForeignKey("animes.Anime", on_delete=models.CASCADE, blank=False, null=False)
    episode = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return self.anime.title