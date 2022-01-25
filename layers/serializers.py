from rest_framework import serializers
from .models import ShapeLayers

class ShapeLayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShapeLayers
        fields = ['id', 'name', 'table_name',]