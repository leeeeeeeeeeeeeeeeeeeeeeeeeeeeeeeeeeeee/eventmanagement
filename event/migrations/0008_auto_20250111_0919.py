# Generated by Django 3.0 on 2025-01-11 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20250108_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='crowd',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='appointments',
            name='hour',
            field=models.CharField(default='', max_length=100),
        ),
    ]
