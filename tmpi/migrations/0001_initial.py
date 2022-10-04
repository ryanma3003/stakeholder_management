# Generated by Django 4.0.4 on 2022-09-16 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('month', '0001_initial'),
        ('compro', '0010_alter_stakeholder_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tmpi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('year', models.IntegerField()),
                ('file_tmpi', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('penilaian_kritikalitas', models.FloatField()),
                ('analisis_ancaman', models.FloatField()),
                ('orang_proses_teknologi', models.FloatField()),
                ('lingkungan_kontrol', models.FloatField()),
                ('penilaian_kematangan', models.FloatField()),
                ('total_fase_1', models.FloatField()),
                ('identifikasi_respon', models.FloatField()),
                ('penyelidikan', models.FloatField()),
                ('aksi', models.FloatField()),
                ('pemulihan', models.FloatField()),
                ('total_fase_2', models.FloatField()),
                ('identifikasi_tindak_lanjut', models.FloatField()),
                ('pelaporan_review', models.FloatField()),
                ('pembelajaran', models.FloatField()),
                ('pembaruan_informasi', models.FloatField()),
                ('analisis_tren', models.FloatField()),
                ('total_fase_3', models.FloatField()),
                ('nilai_akhir', models.FloatField()),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='month.month')),
                ('stakeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compro.stakeholder')),
            ],
        ),
    ]