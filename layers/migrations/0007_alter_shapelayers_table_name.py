# Generated by Django 3.2.9 on 2022-01-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0006_shapelayers_table_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shapelayers',
            name='table_name',
            field=models.CharField(max_length=255, verbose_name='Table name'),
        ),
    ]
