# Generated by Django 3.0.6 on 2020-07-22 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_auto_20200616_1149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-starts_at',)},
        ),
    ]
