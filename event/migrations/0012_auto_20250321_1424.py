# Generated by Django 3.0 on 2025-03-21 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0011_auto_20250321_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='USER',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='signuptable',
        ),
    ]
