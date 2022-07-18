# Generated by Django 3.2.9 on 2022-07-18 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senris', '0013_incident_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='damage',
            name='namesi',
            field=models.CharField(default='', max_length=512, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='damage',
            name='nameta',
            field=models.CharField(default='', max_length=512, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='sensitiveentity',
            name='namesi',
            field=models.CharField(default='', max_length=512, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='sensitiveentity',
            name='nameta',
            field=models.CharField(default='', max_length=512, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='damage',
            name='name',
            field=models.CharField(default='', max_length=512, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='sensitiveentity',
            name='name',
            field=models.CharField(default='', max_length=512, verbose_name='Name'),
        ),
    ]
