# Generated by Django 3.2.9 on 2022-07-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0002_auto_20220205_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtectedArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('constatus', models.CharField(blank=True, max_length=128, null=True)),
                ('owner', models.CharField(blank=True, max_length=128, null=True)),
                ('area', models.FloatField()),
                ('gaz_no', models.CharField(blank=True, max_length=128, null=True)),
                ('date_gaz', models.CharField(blank=True, max_length=128, null=True)),
                ('category', models.CharField(blank=True, max_length=128, null=True)),
                ('remarkes', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='shapelayers',
            name='layerof',
            field=models.IntegerField(choices=[(1, 'Mannar_District_boundary'), (2, 'Mannar_DS_boundary'), (3, 'Mannar_GN_boundary'), (4, 'Mannar_Declared_forest'), (5, 'Mannar_Forest_cover'), (6, 'Mannar_Landuse'), (7, 'Mannar_Major_irr_tank'), (8, 'Mannar_Other_state_forest'), (9, 'Mannar_PA_cover'), (10, 'Mannar_Place'), (11, 'Mannar_River_basin_boundary'), (12, 'Mannar_River_stream'), (13, 'Mannar_Road'), (14, 'Mannar_Slope'), (15, 'Mannar_Small_irr_tank'), (16, 'Ampara_Declared_forest'), (17, 'Ampara_Disrict_boundary'), (18, 'Ampara_DS_boundary'), (19, 'Ampara_Forest_cover'), (20, 'Ampara_GN_boundary'), (21, 'Ampara_Landuse'), (22, 'Ampara_Major_irr_tank'), (23, 'Ampara_Other_state_forest'), (24, 'Ampara_Place'), (25, 'Ampara_River_basin_boundary'), (26, 'Ampara_River_stream'), (27, 'Ampara_Road'), (28, 'Ampara_Slope'), (29, 'Ampara_Small_irr_tank'), (30, 'Ampara_PA_Cover'), (31, 'ProtectedArea')], default=1),
        ),
    ]
