# Generated by Django 4.2.6 on 2023-12-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrineApp', '0013_participation_client_secret_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
