# Generated by Django 3.2.9 on 2022-03-30 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('senris', '0002_incident_admin_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='admin_area',
            new_name='gnd_dsd',
        ),
    ]