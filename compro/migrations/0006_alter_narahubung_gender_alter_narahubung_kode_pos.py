# Generated by Django 4.0.4 on 2022-06-08 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compro', '0005_sistemelektronik_prosedur_narahubung_csirt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narahubung',
            name='gender',
            field=models.CharField(choices=[('m', 'Laki-laki'), ('f', 'Perempuan')], max_length=1),
        ),
        migrations.AlterField(
            model_name='narahubung',
            name='kode_pos',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
