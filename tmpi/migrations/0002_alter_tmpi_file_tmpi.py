# Generated by Django 4.0.4 on 2022-09-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmpi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmpi',
            name='file_tmpi',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
