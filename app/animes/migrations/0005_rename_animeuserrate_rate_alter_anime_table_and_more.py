# Generated by Django 5.0.2 on 2024-03-24 09:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0004_alter_anime_options_alter_animeuserrate_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AnimeUserRate',
            new_name='Rate',
        ),
        migrations.AlterModelTable(
            name='anime',
            table='animes',
        ),
        migrations.AlterModelTable(
            name='format',
            table='formats',
        ),
        migrations.AlterModelTable(
            name='genre',
            table='genres',
        ),
        migrations.AlterModelTable(
            name='list',
            table='lists',
        ),
        migrations.AlterModelTable(
            name='rate',
            table='rates',
        ),
        migrations.AlterModelTable(
            name='studio',
            table='studios',
        ),
    ]