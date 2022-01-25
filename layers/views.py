from logging import NullHandler
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ShapeLayers
from .serializers import ShapeLayerSerializers

def LayerView(request):
    transformer = ShapeLayers.objects.all()
    serializer = ShapeLayerSerializers(transformer, many=True)
    return JsonResponse(serializer.data, safe=False)
