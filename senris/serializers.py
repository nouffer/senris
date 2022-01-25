from rest_framework_gis.serializers import GeoFeatureModelSerializer
from sqlalchemy.sql.functions import mode
from .models import Incident
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