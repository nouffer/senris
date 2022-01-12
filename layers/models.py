from django.contrib.gis.db import models
from django.http.request import MediaType
from django.utils.translation import gettext_lazy as _
import datetime


class MannarDistrictBoundary(models.Model):
    name = models.CharField(_("District name"), max_length=255)
    file = models.FileField(upload_to='%y%m%d', blank=True)
    uploaded_date = models.DateField(default=datetime.date.today)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


# class MannarDSBoundary(models.Model):
#     name = models.CharField(_("DS Name"), max_length=255)
#     geom = models.MultiPolygonField(srid=4326)

#     def __str__(self):
#         return self.name


# class MannarGNBoundary(models.Model):
#     name = models.CharField(_("GND Name"), max_length=255)
#     num = models.CharField(_("GND Number"), max_length=255)
#     geom = models.MultiPolygonField(srid=4326)

#     def __str__(self):
#         return self.name


# class MannarForestCover(models.Model):
#     forest_type = models.CharField(_("Forest Type"), max_length=256)
#     geom = models.MultiPolygonField(srid=4326)

#     def __str__(self):
#         return self.forest_type


# class MannarIrrigationTank(models.Model):
#     name = models.CharField(_("Tank Name"), max_length=256)
#     geom = models.MultiPolygonField(srid=4326)

#     def __str__(self):
#         return self.name


# class MannarLanduse(models.Model):
#     mcode = models.CharField(_("MCode"), max_length=10)
#     scode = models.CharField(_("SCode"), max_length=10)
#     main_category = models.IntegerField(_("Main Category"))
#     sub_category = models.CharField(_("Sub Category"), max_length=10)
#     year_of_update = models.IntegerField(_('year'))
#     geom = models.MultiPolygonField(srid=4326)

#     def __str__(self):
#         return self.mcode


# class MannarNationalRoadNetwork(models.Model):
#     name = models.CharField(_("Road Name"), max_length=256)
#     road_class = models.CharField(_("Road Class"), max_length=10)
#     road_type = models.CharField(_("Road Type"), max_length=10)
#     starts_at = models.CharField(_("Starts At"), max_length=256)
#     ends_at = models.CharField(_("Ends At"), max_length=256)
#     geom = models.MultiLineStringField()

#     def __str__(self):
#         return self.name


# class MannarPACover(models.Model):
#     name = models.CharField(_("Name"), max_length=256)
#     con_status = models.CharField(_("Con Status"), max_length=256)
#     owner = models.CharField(_("Owner"), max_length=256)
#     gaz_no = models.CharField(_("GAZ Num"), max_length=256)
#     date_of_gaz = models.DateField(_("Date of gaz"))
#     category = models.CharField(_("Category"), max_length=256)
#     remarke = models.CharField(_("Remarks"), max_length=512)
#     geom = models.MultiPolygonField(srid=4326)

#     def __str__(self):
#         return self.name

    
# class MannarPlaces(models.Model):
#     name = models.CharField(_("Name"), max_length=256)
#     geom = models.PointField(srid=4326)

#     def __str__(self):
#         return self.name


    
# class MannarRemainingForest(models.Model):
#     forest_type = models.CharField(_("Forest type"), max_length=256)
#     geom = models.MultiPolygonField(srid=4326)

#     def __str__(self):
#         return self.forest_type


# class MannarRiverBasin(models.Model):
#     name = models.CharField(_("Name"), max_length=256)
#     geom = models.MultiPolygonField(srid=4326)

#     def __str__(self):
#         return self.name


# class MannarSmallIrrigationTank(models.Model):
#     name = models.CharField(_("Name"), max_length=256)
#     ownership = models.CharField(_("Ownership"), max_length=256)
#     geom = models.MultiPolygonField(srid=4326)

#     def __str__(self):
#         return self.name