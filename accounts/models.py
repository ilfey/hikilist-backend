from django.db import models

from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __str__(self):
        return self.username