# Generated by Django 3.0.6 on 2020-05-21 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20200519_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='holder',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
