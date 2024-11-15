# Generated by Django 4.0.4 on 2022-08-04 10:21

from django.db import migrations, models
import se.validators


class Migration(migrations.Migration):

    dependencies = [
        ('se', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='se',
            name='bobot_dampak_kegagalan',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='se',
            name='bobot_data_pribadi',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='se',
            name='bobot_kewajiban',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='se',
            name='bobot_kriptografi',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='se',
            name='bobot_kritis_data',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='se',
            name='bobot_kritis_proses',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='se',
            name='bobot_nilai_investasi',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='se',
            name='bobot_pengguna',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='se',
            name='bobot_potensi_kerugian',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='se',
            name='bobot_total_anggaran',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='se',
            name='dampak_kegagalan',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.AddField(
            model_name='se',
            name='data_pribadi',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.AddField(
            model_name='se',
            name='jenis_usaha',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='se',
            name='kewajiban',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.AddField(
            model_name='se',
            name='kriptografi',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.AddField(
            model_name='se',
            name='kritis_data',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.AddField(
            model_name='se',
            name='kritis_proses',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.AddField(
            model_name='se',
            name='nilai_investasi',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.AddField(
            model_name='se',
            name='pengguna',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.AddField(
            model_name='se',
            name='potensi_kerugian',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.AddField(
            model_name='se',
            name='total_anggaran',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1),
        ),
        migrations.AlterField(
            model_name='se',
            name='indeks_nilai',
            field=models.FloatField(blank=True, validators=[se.validators.validate_indeks_nilai]),
        ),
    ]
