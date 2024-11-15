# Generated by Django 4.0.4 on 2022-09-28 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phrasalword',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('passphrase', models.CharField(blank=True, max_length=250, null=True)),
                ('unit_kerja', models.CharField(blank=True, max_length=250, null=True)),
                ('jabatan', models.CharField(blank=True, max_length=250, null=True)),
                ('golongan', models.CharField(blank=True, choices=[('IIa', 'IIa'), ('IIb', 'IIb'), ('IIc', 'IIc'), ('IId', 'IId'), ('IIIa', 'IIIa'), ('IIIb', 'IIIb'), ('IIIc', 'IIIc'), ('IIId', 'IIId'), ('IVa', 'IVa'), ('IVb', 'IVb'), ('IVc', 'IVc'), ('IVd', 'IVd'), ('IVe', 'IVe')], max_length=10, null=True)),
            ],
        ),
    ]
