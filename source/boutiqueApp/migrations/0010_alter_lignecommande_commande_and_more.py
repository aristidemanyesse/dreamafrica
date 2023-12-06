# Generated by Django 4.2.6 on 2023-12-02 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boutiqueApp', '0009_commande_client_secret_alter_lignecommande_quantite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lignecommande',
            name='commande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ligne_commande', to='boutiqueApp.commande'),
        ),
        migrations.AlterField(
            model_name='lignecommande',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ligne_produit', to='boutiqueApp.produit'),
        ),
    ]
