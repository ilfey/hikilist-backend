# Generated by Django 5.0.2 on 2024-03-26 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.anime')),
            ],
        ),
    ]
