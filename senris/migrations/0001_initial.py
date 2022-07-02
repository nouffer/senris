# Generated by Django 3.2.9 on 2022-03-30 18:48

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Layer Name')),
                ('description', models.CharField(blank=True, max_length=512, verbose_name='Layer description')),
                ('file', models.FileField(blank=True, upload_to='%y%m%d')),
                ('uploaded_date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name_plural': 'Layers',
            },
        ),
        migrations.CreateModel(
            name='SensitiveEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siviarity', models.CharField(blank=True, max_length=256, null=True, verbose_name='siviority')),
                ('location_ref', models.CharField(blank=True, max_length=256, null=True, verbose_name='location_ref')),
                ('image1', models.FileField(blank=True, null=True, upload_to='%y%m%d')),
                ('image2', models.FileField(blank=True, null=True, upload_to='%y%m%d')),
                ('image3', models.FileField(blank=True, null=True, upload_to='%y%m%d')),
                ('image4', models.FileField(blank=True, null=True, upload_to='%y%m%d')),
                ('note', models.CharField(blank=True, max_length=512, null=True, verbose_name='note')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('damage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='senris.damage')),
                ('entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='senris.sensitiveentity')),
            ],
        ),
    ]