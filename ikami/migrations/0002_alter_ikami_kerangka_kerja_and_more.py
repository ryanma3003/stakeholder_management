# Generated by Django 4.1.1 on 2022-10-04 04:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikami', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ikami',
            name='kerangka_kerja',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(159)]),
        ),
        migrations.AlterField(
            model_name='ikami',
            name='pengelolaan_aset',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(168)]),
        ),
        migrations.AlterField(
            model_name='ikami',
            name='pengelolaan_risiko',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(72)]),
        ),
        migrations.AlterField(
            model_name='ikami',
            name='tata_kelola',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(126)]),
        ),
        migrations.AlterField(
            model_name='ikami',
            name='teknologi_keamanan',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)]),
        ),
    ]