# Generated by Django 4.2.5 on 2023-10-11 04:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLogin', '0003_alter_client_lastnames_alter_client_names_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='heightPosition',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='record',
            name='widthPosition',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]