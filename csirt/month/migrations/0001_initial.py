# Generated by Django 4.0.4 on 2022-05-23 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('month_id', models.CharField(blank=True, max_length=255)),
                ('month_en', models.CharField(blank=True, max_length=255)),
                ('month_abb', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
