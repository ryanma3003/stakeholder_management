# Generated by Django 4.1.1 on 2022-10-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compro', '0014_stakeholder_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='listworkshop',
            name='level',
            field=models.CharField(blank=True, choices=[('bsc', 'Basic'), ('int', 'Intermediate'), ('adv', 'Advance')], max_length=3, null=True),
        ),
    ]
