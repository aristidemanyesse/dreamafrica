# Generated by Django 4.2.6 on 2023-12-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrineApp', '0014_alter_participation_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]