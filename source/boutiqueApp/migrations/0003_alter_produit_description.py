# Generated by Django 4.2.3 on 2023-08-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutiqueApp', '0002_alter_produit_image1_alter_produit_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
