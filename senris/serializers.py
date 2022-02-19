from pyexpat import model
from attr import field, fields
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from sqlalchemy.sql.functions import mode
from .models import Incident, Damage, SensitiveEntity
from drf_extra_fields.fields import Base64ImageField


class IncidentSerializer(GeoFeatureModelSerializer):
    image1 = Base64ImageField(max_length=None, use_url=True)
    image2 = Base64ImageField(max_length=None, use_url=True)
    image3 = Base64ImageField(max_length=None, use_url=True)
    image4 = Base64ImageField(max_length=None, use_url=True)
    class Meta:
        model=Incident
        geo_field="location"
        fields="__all__"
        #fields=('entity', 'gnd_dsd', 'damage', 'siviarity', 'location_ref', 'note', 'image1', 'image2', 'image3', 'image4')


class DamageSerializer(serializers.ModelSerializer):

    class Meta:
        model=Damage
        fields="__all__"


class SensitiveEntitySerializer(serializers.ModelSerializer):

    class Meta:
        model=SensitiveEntity
        fields="__all__"