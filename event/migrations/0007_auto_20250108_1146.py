# Generated by Django 3.0 on 2025-01-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_signuptable_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signuptable',
            name='portfolio',
        ),
        migrations.AddField(
            model_name='eventteam',
            name='portfolio',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
