# Generated by Django 3.0.6 on 2020-06-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_auto_20200601_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=64),
        ),
    ]
