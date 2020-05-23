# Generated by Django 3.0.6 on 2020-05-17 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='etype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.EventType', verbose_name='Event type'),
        ),
        migrations.AlterField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(default='thumbnails/none/placeholder.jpg', upload_to='thumbnails'),
        ),
    ]