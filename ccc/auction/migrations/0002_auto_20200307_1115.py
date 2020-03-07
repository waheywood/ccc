# Generated by Django 3.0.4 on 2020-03-07 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date'),
        ),
        migrations.AddField(
            model_name='auction',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]