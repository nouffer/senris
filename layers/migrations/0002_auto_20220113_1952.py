# Generated by Django 3.2.9 on 2022-01-13 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='District name')),
                ('file', models.FileField(blank=True, upload_to='%y%m%d')),
                ('uploaded_date', models.DateField(default=datetime.date.today)),
                ('layerof', models.IntegerField(choices=[(1, 'Mannar District boundary'), (2, 'Mannar DS Boundary'), (3, 'Mannar GN boundary'), (4, 'Mannar Forestcover'), (5, 'Mannar irrigation tank'), (6, 'Mannar Landuse'), (7, 'Mannar Roads'), (8, 'Mannar PACover'), (9, 'Mannar Places'), (10, 'Mannar Remaining Forest'), (11, 'Mannar River basin'), (12, 'Mannar Small Irrigation Tanks Point'), (12, 'Mannar Small Irrigation Tanks Polygon')], default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='MannarDSBoundary',
        ),
        migrations.DeleteModel(
            name='MannarForestCover',
        ),
        migrations.DeleteModel(
            name='MannarGNBoundary',
        ),
        migrations.DeleteModel(
            name='MannarIrrigationTank',
        ),
        migrations.DeleteModel(
            name='MannarLanduse',
        ),
        migrations.DeleteModel(
            name='MannarNationalRoadNetwork',
        ),
        migrations.DeleteModel(
            name='MannarPACover',
        ),
        migrations.DeleteModel(
            name='MannarPlaces',
        ),
        migrations.DeleteModel(
            name='MannarRemainingForest',
        ),
        migrations.DeleteModel(
            name='MannarRiverBasin',
        ),
        migrations.DeleteModel(
            name='MannarSmallIrrigationTank',
        ),
        migrations.AlterModelOptions(
            name='mannardistrictboundary',
            options={'verbose_name_plural': 'MannarDistrictBoundaries'},
        ),
    ]
