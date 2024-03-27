from django.db import models

from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"


class Rate(models.Model):
    user = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=False, null=True
    )
    anime = models.ForeignKey(
        "animes.Anime", on_delete=models.CASCADE, blank=False, null=False
    )
    list = models.ForeignKey(
        "accounts.List", on_delete=models.SET_NULL, blank=False, null=True
    )
    rating = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.user}, {self.anime}"

    class Meta:
        db_table = "rates"
        ordering = ["id"]
        constraints = [
            models.UniqueConstraint(fields=["user", "anime"], name="unique_user_anime"),
        ]


class List(models.Model):
    title = models.TextField(max_length=256, blank=False, null=False)
    is_primary = models.BooleanField(blank=False, null=False, default=False)
    user = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=False, null=True
    )

    def __str__(self):
        return f"{self.user} {self.title}"

    class Meta:
        db_table = "lists"
        ordering = ["id"]
