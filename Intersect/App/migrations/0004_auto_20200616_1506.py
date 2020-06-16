# Generated by Django 3.0.5 on 2020-06-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200616_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='Friends',
        ),
        migrations.AddField(
            model_name='account',
            name='Friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='_account_Friends_+', to='App.Account'),
        ),
    ]