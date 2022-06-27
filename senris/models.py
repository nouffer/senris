from email.policy import default
from ntpath import realpath
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
from django.contrib.auth.models import User

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

###################### incident  ###########################

DAMAGE = (
    (1, _("Encroachments")),
    (2, _("Mining")),
    (3, _("Filling of Land")),
    (4, _("Damages to the Mangroves")),
    (5, _("Poaching and Traps")),
    (6, _("Forest Fires")),
    (7, _("Other natural resources")),
    (8, _("impacts on the livelihood of communities")),
    (9, _("Poaching")),
    (10, _("Illegal Traps")),
    (11, _("Illegal electric fences")),
    (12, _("Intentional forest fires")),
    (13, _("Other"))
)

class Damage(models.Model):
    name=models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name


class SensitiveEntity(models.Model):
    name=models.CharField(_("Name"), max_length=255)
    color_code = models.CharField(_("Hex color code"), max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class Incident(models.Model):

    entity = models.ForeignKey('SensitiveEntity', related_name='entity', on_delete=models.CASCADE, blank=True, null=True)
    damage=models.ForeignKey('Damage', related_name='damage', on_delete=models.CASCADE, blank=True, null=True)
    gnd_dsd = models.CharField("gnd_dsd",max_length=256, blank=True, null=True )
    siviarity=models.CharField(_("siviority"), max_length=256, blank=True, null=True)
    location_ref=models.CharField(_("location_ref"), max_length=256, blank=True, null=True)
    is_approved = models.BooleanField(_("Is Approved"), default=False)
    image1=models.FileField(upload_to='%y%m%d', blank=True, null=True)
    image2=models.FileField(upload_to='%y%m%d', blank=True, null=True)
    image3=models.FileField(upload_to='%y%m%d', blank=True, null=True)
    image4=models.FileField(upload_to='%y%m%d', blank=True, null=True)
    note=models.CharField(_("note"), max_length=512, blank=True, null=True)
    contact=models.CharField(_("Contact No"), max_length=512, blank=True, null=True)
    location=models.PointField()
    reporter = models.ForeignKey(User, related_name="reported_user", on_delete=models.DO_NOTHING, blank=True, null=True)
    collected_location=models.PointField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
