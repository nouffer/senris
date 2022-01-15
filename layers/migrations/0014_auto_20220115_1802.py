# Generated by Django 3.2.9 on 2022-01-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0013_auto_20220115_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mannarpacover',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='mannarriverbasin',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='mannarsmallirrigationtankpoint',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='mannarsmallirrigationtankpoly',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='mannarstreamnetwork',
            name='object_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
