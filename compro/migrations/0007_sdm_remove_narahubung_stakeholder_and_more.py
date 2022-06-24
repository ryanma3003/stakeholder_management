# Generated by Django 4.0.4 on 2022-06-12 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compro', '0006_alter_narahubung_gender_alter_narahubung_kode_pos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sdm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=255)),
                ('jabatan', models.CharField(blank=True, max_length=255, null=True)),
                ('unit_kerja', models.CharField(blank=True, max_length=255, null=True)),
                ('kompetensi', models.TextField(blank=True, null=True)),
                ('sertifikat', models.TextField(blank=True, null=True)),
                ('telepon', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(default='info@corporate.com', max_length=255)),
                ('csirt', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=5)),
                ('narahubung', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=5)),
                ('gender', models.CharField(choices=[('m', 'Laki-laki'), ('f', 'Perempuan')], max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='narahubung',
            name='stakeholder',
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='kode_pos',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='landing_page',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Csirt',
        ),
        migrations.DeleteModel(
            name='Narahubung',
        ),
        migrations.AddField(
            model_name='sdm',
            name='stakeholder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compro.stakeholder'),
        ),
    ]