from django.contrib.gis.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
import datetime
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
import geopandas as gpd
from sqlalchemy import *
from geoalchemy2 import Geometry, WKTElement
import os, zipfile, glob
import environ
from geo.Geoserver import Geoserver
from geo.Postgres import Db
from sqlalchemy.sql.functions import mode
from layers.choices import LAYER_CHOICES
from django.contrib.gis.utils import LayerMapping
from pathlib import Path
from .mapping import mannar_district_boundary_mapping, mannar_dsd_mapping, mannar_gnd_mapping, mannar_forest_cover_mapping , mannar_irrigation_tank_mapping , mannar_landuse_mapping , mannar_national_roads_mapping , mannar_pa_cover_mapping , mannar_places_mapping , mannar_remaining_forest_mapping , mannar_river_basin_mapping , mannar_small_irrigation_tank_point_mapping , mannar_small_irrigation_tank_poly_mapping , mannar_stream_network_mapping 

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=".env")

db = Db(dbname=env("POSTGRES_DBNAME"), user=env("POSTGRES_USER"), password=env("POSTGRES_PASS"), host="postgres-db", port=env("PG_PORT"))
geo = Geoserver('http://geoserver:8080/geoserver', username=env("GEOSERVER_ADMIN_USER"), password=env("GEOSERVER_ADMIN_PASSWORD"))


class MannarDistrictBoundary(models.Model):
    name = models.CharField(_("District name"), max_length=255)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = "MannarDistrictBoundaries"

    def __str__(self):
        return self.name


class MannarDSBoundary(models.Model):
    name = models.CharField(_("DSD Name"), max_length=255)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


class MannarGNBoundary(models.Model):
    name = models.CharField(_("GND Name"), max_length=255)
    num = models.CharField(_("GND Number"), max_length=255, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


class MannarForestCover(models.Model):
    forest_type = models.CharField(_("Forest Type"), max_length=256)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.forest_type


class MannarIrrigationTank(models.Model):
    name = models.CharField(_("Tank Name"), max_length=256)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


class MannarLanduse(models.Model):
    mcode = models.CharField(_("MCode"), max_length=10, null=True, blank=True)
    scode = models.CharField(_("SCode"), max_length=10, null=True, blank=True)
    main_category = models.IntegerField(_("Main Category"), null=True, blank=True)
    sub_category = models.CharField(_("Sub Category"), max_length=10, null=True, blank=True)
    year_of_update = models.IntegerField(_('year'), null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.mcode


class MannarNationalRoadNetwork(models.Model):
    name = models.CharField(_("Road Name"), max_length=256, null=True, blank=True)
    road_class = models.CharField(_("Road Class"), max_length=10, null=True, blank=True)
    road_type = models.CharField(_("Road Type"), max_length=10, null=True, blank=True)
    starts_at = models.CharField(_("Starts At"), max_length=256, null=True, blank=True)
    ends_at = models.CharField(_("Ends At"), max_length=256, null=True, blank=True)
    geom = models.MultiLineStringField()

    def __str__(self):
        return self.name


class MannarPACover(models.Model):
    name = models.CharField(_("Name"), max_length=256, null=True, blank=True)
    con_status = models.CharField(_("Con Status"), max_length=256, null=True, blank=True)
    owner = models.CharField(_("Owner"), max_length=256, null=True, blank=True)
    gaz_no = models.CharField(_("GAZ Num"), max_length=256, null=True, blank=True)
    date_of_gaz = models.CharField(_("Date of gaz"), max_length=256, null=True, blank=True)
    category = models.CharField(_("Category"), max_length=256, null=True, blank=True)
    remarke = models.CharField(_("Remarks"), max_length=512, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    
class MannarPlaces(models.Model):
    name = models.CharField(_("Name"), max_length=256)
    geom = models.PointField(srid=4326)


    
class MannarRemainingForest(models.Model):
    forest_type = models.CharField(_("Forest type"), max_length=256)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.forest_type


class MannarRiverBasin(models.Model):
    name = models.CharField(_("Name"), max_length=256, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)



class MannarSmallIrrigationTankPoint(models.Model):
    name = models.CharField(_("Name"), max_length=256, null=True, blank=True)
    river_b_na = models.CharField(_("River B Na"), max_length=256, null=True, blank=True)
    ownership = models.CharField(_("Ownership"), max_length=256, null=True, blank=True)
    functional = models.CharField(_("Functional"), max_length=256, null=True, blank=True)
    remarke = models.CharField(_("Remarks"), max_length=512, null=True, blank=True)
    geom = models.PointField(srid=4326)
        

class MannarSmallIrrigationTankPoly(models.Model):
    name = models.CharField(_("Name"), max_length=256, null=True, blank=True)
    river_b_na = models.CharField(_("River B Na"), max_length=256, null=True, blank=True)
    ownership = models.CharField(_("Ownership"), max_length=256, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)



class MannarStreamNetwork(models.Model):
    object_id = models.IntegerField(null=True, blank=True)
    from_node = models.IntegerField(null=True, blank=True)
    to_node = models.IntegerField(null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)







def getTableForModel(tbl):
    if tbl == 1:
        return MannarDistrictBoundary.objects.model._meta.db_table;
    elif tbl == 2:
        return MannarDSBoundary.objects.model._meta.db_table
    elif tbl == 3:
        return MannarGNBoundary.objects.model._meta.db_table;
    elif tbl == 4:
        return MannarForestCover.objects.model._meta.db_table;
    elif tbl == 5:
        return MannarIrrigationTank.objects.model._meta.db_table;
    elif tbl == 6:
        return MannarLanduse.objects.model._meta.db_table;
    elif tbl == 7:
        return MannarNationalRoadNetwork.objects.model._meta.db_table;
    elif tbl == 8:
        return MannarPACover.objects.model._meta.db_table;
    elif tbl == 9:
        return MannarPlaces.objects.model._meta.db_table;
    elif tbl == 10:
        return MannarRemainingForest.objects.model._meta.db_table;
    elif tbl == 11:
        return MannarRiverBasin.objects.model._meta.db_table;
    elif tbl == 12:
        return MannarSmallIrrigationTankPoint.objects.model._meta.db_table;
    elif tbl == 13:
        return MannarSmallIrrigationTankPoly.objects.model._meta.db_table;
    else:
        return MannarStreamNetwork.objects.model._meta.db_table;
        



def getMappingforModel(tbl, shp):
    if tbl == 1:
        return LayerMapping(MannarDistrictBoundary, shp, mannar_district_boundary_mapping, transform=False)
    elif tbl == 2:
        return LayerMapping(MannarDSBoundary, shp, mannar_dsd_mapping, transform=False)
    elif tbl == 3:
        return LayerMapping(MannarGNBoundary, shp, mannar_gnd_mapping, transform=False)
    elif tbl == 4:
        return LayerMapping(MannarForestCover, shp, mannar_forest_cover_mapping, transform=False)
    elif tbl == 5:
        return LayerMapping(MannarIrrigationTank, shp, mannar_irrigation_tank_mapping, transform=False)
    elif tbl == 6:
        return LayerMapping(MannarLanduse, shp, mannar_landuse_mapping, transform=False)
    elif tbl == 7:
        return LayerMapping(MannarNationalRoadNetwork, shp, mannar_national_roads_mapping, transform=False)
    elif tbl == 8:
        return LayerMapping(MannarPACover, shp, mannar_pa_cover_mapping, transform=False)
    elif tbl == 9:
        return LayerMapping(MannarPlaces, shp, mannar_places_mapping, transform=False)
    elif tbl == 10:
        return LayerMapping(MannarRemainingForest, shp, mannar_remaining_forest_mapping, transform=False)
    elif tbl == 11:
        return LayerMapping(MannarRiverBasin, shp, mannar_river_basin_mapping, transform=False)
    elif tbl == 12:
        return LayerMapping(MannarSmallIrrigationTankPoint, shp, mannar_small_irrigation_tank_point_mapping, transform=False)
    elif tbl == 13:
        return LayerMapping(MannarSmallIrrigationTankPoly, shp, mannar_small_irrigation_tank_poly_mapping, transform=False)
    else:
        return LayerMapping(MannarStreamNetwork, shp, mannar_stream_network_mapping, transform=False)

class ShapeLayers(models.Model):
    name = models.CharField(_("District name"), max_length=255)
    file = models.FileField(upload_to='%y%m%d', blank=True)
    uploaded_date = models.DateField(default=datetime.date.today)
    layerof = models.IntegerField(choices=LAYER_CHOICES, default=1)
    table_name = models.CharField(_("Table name"), max_length=255, blank=True)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=ShapeLayers)
def my_callback(sender, instance, *args, **kwargs):
    instance.table_name = getTableForModel(instance.layerof)

@receiver(post_save, sender=ShapeLayers)
def publish_date(sender, instance, created, **kwargs):
    file = instance.file.path
    file_format = os.path.basename(file).split('.')[-1]
    file_name = os.path.basename(file).split('.')[0]
    file_path = os.path.dirname(file)
    name = instance.name
    conn_str = f'postgresql://{env("POSTGRES_USER")}:{env("POSTGRES_PASS")}@{env("PG_HOST")}:{env("PG_PORT")}/{env("POSTGRES_DBNAME")}'

    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(file_path)
    
    os.remove(file)

    try:
        shp = glob.glob(r'{}/**/*.shp'.format(file_path), recursive=True)[0]
        gdf = gpd.read_file(shp)
        crs_name = str(gdf.crs.srs)
        print(crs_name, 'crs - name')
        epsg = int(crs_name.replace('epsg:',''))
        if epsg is None:
            epsg=4326

        print("### shape file is ###")

        lm2 = getMappingforModel(instance.layerof, shp)
        lm2.save(strict=True, verbose=True)

        #lm=LayerMapping(MannarDistrictBoundary, shp, mannar_district_boundary_mapping, transform=False)
        #lm.save(strict=True, verbose=True)

        print("### afte save ###")

        geo.create_featurestore(store_name='geo_data', workspace='demo', db=env("POSTGRES_DBNAME"), host='postgres-db', pg_user=env("POSTGRES_USER"), pg_password=env("POSTGRES_PASS"), schema='public')
        geo.publish_featurestore(workspace='demo', store_name='geo_data', pg_table=getTableForModel(instance.layerof))

        os.remove(shp)
    except Exception as e:
        print('##################',e)


@receiver(post_delete, sender=ShapeLayers)
def delete_layer(sender, instance, **kwargs):
    # db.delete_table(table_name=instance.name, schema='public')
    geo.delete_layer(instance.name, "demo")

