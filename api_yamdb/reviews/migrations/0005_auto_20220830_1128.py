# Generated by Django 2.2.16 on 2022-08-30 08:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20220828_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveIntegerField(default=1, help_text='Оценка произведения', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Оценка произведения'),
        ),
    ]