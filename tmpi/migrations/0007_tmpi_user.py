# Generated by Django 4.1.1 on 2022-11-01 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tmpi', '0006_alter_tmpi_file_tmpi'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmpi',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
