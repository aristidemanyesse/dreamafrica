# Generated by Django 4.2.6 on 2023-12-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrineApp', '0016_suggestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='contact',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='fullname',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='objet',
            field=models.CharField(default='', max_length=255),
        ),
    ]