# Generated by Django 4.2.6 on 2023-10-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrineApp', '0011_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='quantite',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]