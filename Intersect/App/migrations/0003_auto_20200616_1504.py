# Generated by Django 3.0.5 on 2020-06-16 09:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20200616_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='Friends',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='False', max_length=200, null=True), size=100),
        ),
    ]
