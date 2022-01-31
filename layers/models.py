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
from .mapping import \
    mannar_river_basin_boundary_mapping, \
    mannar_declared_forest_mapping, \
    mannar_district_boundary_mapping, \
    mannar_ds_boundary_mapping, \
    mannar_forest_cover_mapping, \
    mannar_gn_boundary_mapping, \
    mannar_landuse_mapping, \
    mannar_major_irr_tank_mapping, \
    mannar_other_state_forest_mapping, \
    mannar_pa_cover_mapping, \
    mannar_place_mapping, \
    mannar_river_stream_mapping, \
    mannar_road_mapping, \
    mannar_slope_mapping, \
    mannar_small_irr_tank_mapping,\
    ampara_declared_forest_mapping, \
    ampara_disrict_boundary_mapping, \
    ampara_ds_boundary_mapping, \
    ampara_forest_cover_mapping, \
    ampara_gn_boundary_mapping, \
    ampara_landuse_mapping, \
    ampara_river_stream_mapping, \
    ampara_major_irr_tank_mapping, \
    ampara_place_mapping, \
    ampara_other_state_forest_mapping, \
    ampara_river_basin_boundary_mapping, \
    ampara_road_mapping, \
    ampara_slope_mapping, \
    ampara_small_irr_tank_mapping


env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=".env")

db = Db(dbname=env("POSTGRES_DBNAME"), user=env("POSTGRES_USER"), password=env("POSTGRES_PASS"), host="postgres-db", port=env("PG_PORT"))
geo = Geoserver('http://geoserver:8080/geoserver', username=env("GEOSERVER_ADMIN_USER"), password=env("GEOSERVER_ADMIN_PASSWORD"))


class Mannar_District_boundary(models.Model):
    objectid = models.BigIntegerField(null=True, blank=True)
    district_n = models.CharField(max_length=254, null=True, blank=True)
    shape_leng = models.FloatField(null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)
    
    def __str__(self):
        return str(self.id) + self.district_n
    


class Mannar_DS_boundary(models.Model):
    dsd_n = models.CharField(max_length=254, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.dsd_n
    

class Mannar_GN_boundary(models.Model):
    gnd_n = models.CharField(max_length=254, null=True, blank=True)
    gnd_no = models.CharField(max_length=254, null=True, blank=True)
    district_n = models.CharField(max_length=254, null=True, blank=True)
    dsd_n = models.CharField(max_length=254, null=True, blank=True)
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.gnd_n
    

class Mannar_Declared_forest(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    con_status = models.CharField(max_length=50, null=True, blank=True)
    owner = models.CharField(max_length=10, null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id)
    

class Mannar_Forest_cover(models.Model):
    district = models.CharField(max_length=25, null=True, blank=True)
    area_final = models.FloatField(null=True, blank=True)
    f_type = models.CharField(max_length=25, null=True, blank=True)
    lc = models.CharField(max_length=25, null=True, blank=True)
    forest_typ = models.CharField(max_length=50, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.district


class Mannar_Landuse(models.Model):
    mcode = models.CharField(max_length=50, null=True, blank=True)
    scode = models.CharField(max_length=50, null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    main_land = models.CharField(max_length=100, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.main_land
    

class Mannar_Major_irr_tank(models.Model):
    tank_name = models.CharField(max_length=50, null=True, blank=True)
    map_id = models.BigIntegerField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.tank_name


class Mannar_Other_state_forest(models.Model):
    forest_typ = models.CharField(max_length=50, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.forest_typ


class Mannar_PA_cover(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    con_status = models.CharField(max_length=50, null=True, blank=True)
    owner = models.CharField(max_length=10, null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)


class Mannar_Place(models.Model):
    place_id = models.BigIntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return str(self.id) + self.name

class Mannar_River_basin_boundary(models.Model):
    rb_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    basin_area = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)



class Mannar_River_stream(models.Model):
    objectid = models.IntegerField(null=True, blank=True)
    shape_leng = models.FloatField(null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)


class Mannar_Road(models.Model):
    tl_nm_tran = models.CharField(max_length=50, null=True, blank=True)
    road_class = models.CharField(max_length=30, null=True, blank=True)
    type = models.CharField(max_length=10, null=True, blank=True)
    start = models.CharField(max_length=70, null=True, blank=True)
    end = models.CharField(max_length=70, null=True, blank=True)
    start_km_p = models.FloatField(null=True, blank=True)
    end_km_pos = models.FloatField(null=True, blank=True)
    tot_length = models.FloatField(null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return str(self.id) + self.tl_nm_tran
    

class Mannar_Slope(models.Model):
    slope_id = models.BigIntegerField(null=True, blank=True)
    gridcode = models.BigIntegerField(null=True, blank=True)
    sl_class = models.CharField(max_length=15, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)



class Mannar_Small_irr_tank(models.Model):
    tank_name = models.CharField(max_length=50, null=True, blank=True)
    map_id = models.BigIntegerField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)



class Ampara_Declared_forest(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    con_status = models.CharField(max_length=50, null=True, blank=True)
    owner = models.CharField(max_length=10, null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.name


class Ampara_Disrict_boundary(models.Model):
    district_n = models.CharField(max_length=254, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.district_n


class Ampara_DS_boundary(models.Model):
    dsd_n = models.CharField(max_length=254, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)
    
    def __str__(self):
        return str(self.id) + self.dsd_n


class Ampara_Forest_cover(models.Model):
    forest_cover_id = models.IntegerField(null=True, blank=True)
    lc = models.CharField(max_length=25, null=True, blank=True)
    forest_typ = models.CharField(max_length=50, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.forest_typ

    
class Ampara_GN_boundary(models.Model):
    gnd_n = models.CharField(max_length=254, null=True, blank=True)
    gnd_no = models.CharField(max_length=254, null=True, blank=True)
    district_n = models.CharField(max_length=254, null=True, blank=True)
    dsd_n = models.CharField(max_length=254, null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.gnd_n


class Ampara_Landuse(models.Model):
    mcode = models.CharField(max_length=50, null=True, blank=True)
    scode = models.CharField(max_length=50, null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    main_land = models.CharField(max_length=100, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.main_land

class Ampara_Major_irr_tank(models.Model):
    tank_name = models.CharField(max_length=50, null=True, blank=True)
    map_id = models.BigIntegerField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.tank_name

class Ampara_Other_state_forest(models.Model):
    fid_fc_201 = models.BigIntegerField(null=True, blank=True)
    forest_typ = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.name


class Ampara_Place(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return str(self.id) + self.name

class Ampara_River_basin_boundary(models.Model):
    rb_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    basin_area = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return str(self.id) + self.name

class Ampara_River_stream(models.Model):
    objectid = models.IntegerField(null=True, blank=True)
    shape_leng = models.FloatField(null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)


class Ampara_Road(models.Model):
    tl_nm_tran = models.CharField(max_length=50, null=True, blank=True)
    road_class = models.CharField(max_length=30, null=True, blank=True)
    type = models.CharField(max_length=10, null=True, blank=True)
    start = models.CharField(max_length=70, null=True, blank=True)
    end = models.CharField(max_length=70, null=True, blank=True)
    tot_length = models.FloatField(null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return str(self.id) + self.tl_nm_tran
    

class Ampara_Slope(models.Model):
    slope_id = models.BigIntegerField(null=True, blank=True)
    gridcode = models.BigIntegerField(null=True, blank=True)
    sl_class = models.CharField(max_length=15, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326, null=True, blank=True)


class Ampara_Small_irr_tank(models.Model):
    tank_name = models.CharField(max_length=50, null=True, blank=True)
    map_id = models.BigIntegerField(null=True, blank=True)
    district = models.CharField(max_length=254, null=True, blank=True)
    asc_field = models.CharField(max_length=254, null=True, blank=True)
    gnd = models.CharField(max_length=254, null=True, blank=True)
    river_b_na = models.CharField(max_length=25, null=True, blank=True)
    dsd = models.CharField(max_length=37, null=True, blank=True)
    ownership = models.CharField(max_length=30, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)
    
    
    
def getTableForModel(tbl):
    if tbl == 1:
        return Mannar_District_boundary.objects.model._meta.db_table;
    elif tbl == 2:
        return Mannar_DS_boundary.objects.model._meta.db_table
    elif tbl == 3:
        return Mannar_GN_boundary.objects.model._meta.db_table;
    elif tbl == 4:
        return Mannar_Declared_forest.objects.model._meta.db_table;
    elif tbl == 5:
        return Mannar_Forest_cover.objects.model._meta.db_table;
    elif tbl == 6:
        return Mannar_Landuse.objects.model._meta.db_table;
    elif tbl == 7:
        return Mannar_Major_irr_tank.objects.model._meta.db_table;
    elif tbl == 8:
        return Mannar_Other_state_forest.objects.model._meta.db_table;
    elif tbl == 9:
        return Mannar_PA_cover.objects.model._meta.db_table;
    elif tbl == 10:
        return Mannar_Place.objects.model._meta.db_table;
    elif tbl == 11:
        return Mannar_River_basin_boundary.objects.model._meta.db_table;
    elif tbl == 12:
        return Mannar_River_stream.objects.model._meta.db_table;
    elif tbl == 13:
        return Mannar_Road.objects.model._meta.db_table;
    elif tbl == 14:
        return Mannar_Slope.objects.model._meta.db_table;
    elif tbl == 15:
        return Mannar_Small_irr_tank.objects.model._meta.db_table;
    elif tbl == 16:
        return Ampara_Declared_forest.objects.model._meta.db_table;
    elif tbl == 17:
        return Ampara_Disrict_boundary.objects.model._meta.db_table;
    elif tbl == 18:
        return Ampara_DS_boundary.objects.model._meta.db_table;
    elif tbl == 19:
        return Ampara_Forest_cover.objects.model._meta.db_table;
    elif tbl == 20:
        return Ampara_GN_boundary.objects.model._meta.db_table;
    elif tbl == 21:
        return Ampara_Landuse.objects.model._meta.db_table;
    elif tbl == 22:
        return Ampara_Major_irr_tank.objects.model._meta.db_table;
    elif tbl == 23:
        return Ampara_Other_state_forest.objects.model._meta.db_table;
    elif tbl == 24:
        return Ampara_Place.objects.model._meta.db_table;
    elif tbl == 25:
        return Ampara_River_basin_boundary.objects.model._meta.db_table;
    elif tbl == 26:
        return Ampara_River_stream.objects.model._meta.db_table;
    elif tbl == 27:
        return Ampara_Road.objects.model._meta.db_table;
    elif tbl == 128:
        return Ampara_Slope.objects.model._meta.db_table;
    else:
        return Ampara_Small_irr_tank.objects.model._meta.db_table;
        



def getMappingforModel(tbl, shp):
    if tbl == 1:
        return LayerMapping(Mannar_District_boundary, shp, mannar_district_boundary_mapping, transform=False)
    elif tbl == 2:
        return LayerMapping(Mannar_DS_boundary, shp, mannar_ds_boundary_mapping, transform=False)
    elif tbl == 3:
        return LayerMapping(Mannar_GN_boundary, shp, mannar_gn_boundary_mapping, transform=False)
    elif tbl == 4:
        return LayerMapping(Mannar_Declared_forest, shp, mannar_declared_forest_mapping, transform=False)
    elif tbl == 5:
        return LayerMapping(Mannar_Forest_cover, shp, mannar_forest_cover_mapping, transform=False)
    elif tbl == 6:
        return LayerMapping(Mannar_Landuse, shp, mannar_landuse_mapping, transform=False)
    elif tbl == 7:
        return LayerMapping(Mannar_Major_irr_tank, shp, mannar_major_irr_tank_mapping, transform=False)
    elif tbl == 8:
        return LayerMapping(Mannar_Other_state_forest, shp, mannar_other_state_forest_mapping, transform=False)
    elif tbl == 9:
        return LayerMapping(Mannar_PA_cover, shp, mannar_pa_cover_mapping, transform=False)
    elif tbl == 10:
        return LayerMapping(Mannar_Place, shp, mannar_place_mapping, transform=False)
    elif tbl == 11:
        return LayerMapping(Mannar_River_basin_boundary, shp, mannar_river_basin_boundary_mapping, transform=False)
    elif tbl == 12:
        return LayerMapping(Mannar_River_stream, shp, mannar_river_stream_mapping, transform=False)
    elif tbl == 13:
        return LayerMapping(Mannar_Road, shp, mannar_road_mapping, transform=False)
    elif tbl == 14:
        return LayerMapping(Mannar_Slope, shp, mannar_slope_mapping, transform=False)
    elif tbl == 15:
        return LayerMapping(Mannar_Small_irr_tank, shp, mannar_small_irr_tank_mapping, transform=False)
    elif tbl == 16:
        return LayerMapping(Ampara_Declared_forest, shp, ampara_declared_forest_mapping, transform=False)
    elif tbl == 17:
        return LayerMapping(Ampara_Disrict_boundary, shp, ampara_disrict_boundary_mapping, transform=False)
    elif tbl == 18:
        return LayerMapping(Ampara_DS_boundary, shp, ampara_ds_boundary_mapping, transform=False)
    elif tbl == 19:
        return LayerMapping(Ampara_Forest_cover, shp, ampara_forest_cover_mapping, transform=False)
    elif tbl == 20:
        return LayerMapping(Ampara_GN_boundary, shp, ampara_gn_boundary_mapping, transform=False)
    elif tbl == 21:
        return LayerMapping(Ampara_Landuse, shp, ampara_landuse_mapping, transform=False)
    elif tbl == 22:
        return LayerMapping(Ampara_Major_irr_tank, shp, ampara_major_irr_tank_mapping, transform=False)
    elif tbl == 23:
        return LayerMapping(Ampara_Other_state_forest, shp, ampara_other_state_forest_mapping, transform=False)
    elif tbl == 24:
        return LayerMapping(Ampara_Place, shp, ampara_place_mapping, transform=False)
    elif tbl == 25:
        return LayerMapping(Ampara_River_basin_boundary, shp, ampara_river_basin_boundary_mapping, transform=False)
    elif tbl == 26:
        return LayerMapping(Ampara_River_stream, shp, ampara_river_stream_mapping, transform=False)
    elif tbl == 27:
        return LayerMapping(Ampara_Road, shp, ampara_road_mapping, transform=False)
    elif tbl == 128:
        return LayerMapping(Ampara_Slope, shp, ampara_slope_mapping, transform=False)
    else:
        return LayerMapping(Ampara_Small_irr_tank, shp, ampara_small_irr_tank_mapping, transform=False)

class ShapeLayers(models.Model):
    name = models.CharField(_("Shape Layer"), max_length=255)
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

