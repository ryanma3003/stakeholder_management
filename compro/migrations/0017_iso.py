# Generated by Django 4.1.1 on 2022-12-06 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compro', '0016_remove_listworkshop_sdm_listworkshop_sdm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iso',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stakeholder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='compro.stakeholder')),
                ('status', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
            ],
        ),
    ]
