# Generated by Django 4.2.3 on 2023-08-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutiqueApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image1',
            field=models.ImageField(blank=True, default='images/produits/default.png', max_length=255, null=True, upload_to='images/produits/'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image2',
            field=models.ImageField(blank=True, default='images/produits/default.png', max_length=255, null=True, upload_to='images/produits/'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image3',
            field=models.ImageField(blank=True, default='images/produits/default.png', max_length=255, null=True, upload_to='images/produits/'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image4',
            field=models.ImageField(blank=True, default='images/produits/default.png', max_length=255, null=True, upload_to='images/produits/'),
        ),
    ]
