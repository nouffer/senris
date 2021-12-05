from rest_framework_gis.serializers import GeoFeatureModelSerializer
from sqlalchemy.sql.functions import mode
from .models import Incident

class IncidentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model=Incident
        geo_field="location"
        fields="__all__"