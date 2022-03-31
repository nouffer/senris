from dataclasses import fields
from rest_framework import serializers
from .models import ShapeLayers, Mannar_DS_boundary, Mannar_GN_boundary

class ShapeLayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShapeLayers
        fields = ['id', 'name', 'table_name',]


class MannarDSDSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mannar_DS_boundary
        fields =  ['id', 'dsd_n',]

class MannarGNSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mannar_GN_boundary
        fields= ['id', 'gnd_n', 'gnd_no',]

