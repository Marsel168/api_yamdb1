# Generated by Django 2.2.16 on 2022-08-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True, max_length=256, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(related_name='titles', through='reviews.TitleGenre', to='reviews.Genre', verbose_name='Жанр'),
        ),
    ]
