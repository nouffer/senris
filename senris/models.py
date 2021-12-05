from django.contrib.gis.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import geopandas as gpd
from sqlalchemy import *
from geoalchemy2 import Geometry, WKTElement
import os, zipfile, glob
import environ
from geo.Geoserver import Geoserver
from geo.Postgres import Db
from sqlalchemy.sql.functions import mode

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=".env")

db = Db(dbname=env("POSTGRES_DBNAME"), user=env("POSTGRES_USER"), password=env("POSTGRES_PASS"), host="postgres-db", port=env("PG_PORT"))
geo = Geoserver('http://geoserver:8080/geoserver', username=env("GEOSERVER_ADMIN_USER"), password=env("GEOSERVER_ADMIN_PASSWORD"))

class Layer(models.Model):
    name=models.CharField(_("Layer Name"), max_length=155)
    description = models.CharField(_("Layer description"), max_length=512, blank=True)
    file = models.FileField(upload_to='%y%m%d', blank=True)
    uploaded_date = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name_plural = "Layers"

    def __str__(self):
        return self.name


@receiver(post_save, sender=Layer)
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

        os.remove(shp)
    except Exception as e:
        for s in shp:
           os.remove(s)
    
    #geom_type = gdf.geom_type[1]
    engine = create_engine(conn_str)
    gdf['geom'] = gdf['geometry'].apply(lambda x: WKTElement(x.wkt, srid=epsg))
    gdf.drop('geometry', 1, inplace=True)
    gdf.to_sql(name, engine, 'public', if_exists='replace', index=False, dtype={"geom":Geometry('Geometry', srid=epsg)})

    geo.create_featurestore(store_name='geo_data', workspace='demo', db=env("POSTGRES_DBNAME"), host='postgres-db', pg_user=env("POSTGRES_USER"), pg_password=env("POSTGRES_PASS"), schema='public')
    geo.publish_featurestore(workspace='demo', store_name='geo_data', pg_table=name)

    # geo.create_outline_featurestyle('demo_lyr', workspace='demo')
    # geo.publish_style(layer_name=name, style_name='demo_lyr', workspace='demo')


@receiver(post_delete, sender=Layer)
def delete_layer(sender, instance, **kwargs):
    db.delete_table(table_name=instance.name, schema='public')
    geo.delete_layer(instance.name, "demo")

class District(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class IncidentType(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Incident(models.Model):
    name=models.CharField(max_length=512)
    type=models.ForeignKey(IncidentType, on_delete=CASCADE)
    district=models.ForeignKey(District, on_delete=CASCADE)
    location=models.PointField()

    def __str__(self):
        return self.name

