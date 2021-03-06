# Generated by Django 3.0.4 on 2020-03-07 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auto_20200307_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='starting_bid',
        ),
        migrations.AddField(
            model_name='auction',
            name='highest_bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='highest_bid', to='auction.Bid'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='auction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auction.Auction'),
        ),
    ]
