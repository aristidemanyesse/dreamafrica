# Generated by Django 4.2.6 on 2023-10-16 21:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vitrineApp', '0008_alter_faq_question_alter_faq_reponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('protected', models.BooleanField(default=False)),
                ('fullname', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReservationStand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('protected', models.BooleanField(default=False)),
                ('fullname', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact', models.CharField(default='', max_length=255)),
                ('domaine', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('description', models.TextField(default='')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='jour',
            name='edition',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='type',
        ),
        migrations.RemoveField(
            model_name='stand',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='stand',
            name='edition',
        ),
        migrations.RemoveField(
            model_name='evenement',
            name='code',
        ),
        migrations.RemoveField(
            model_name='evenement',
            name='image',
        ),
        migrations.RemoveField(
            model_name='evenement',
            name='jour',
        ),
        migrations.RemoveField(
            model_name='evenement',
            name='time',
        ),
        migrations.AddField(
            model_name='evenement',
            name='edition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Actualite',
        ),
        migrations.DeleteModel(
            name='CategorieStand',
        ),
        migrations.DeleteModel(
            name='Edition',
        ),
        migrations.DeleteModel(
            name='Jour',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
        migrations.DeleteModel(
            name='Stand',
        ),
        migrations.DeleteModel(
            name='TypeParticipant',
        ),
        migrations.AddField(
            model_name='reservationstand',
            name='evenement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorie_stand', to='vitrineApp.evenement'),
        ),
        migrations.AddField(
            model_name='participation',
            name='evenement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_participant', to='vitrineApp.evenement'),
        ),
    ]
