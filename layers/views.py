from logging import NullHandler
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ShapeLayers, Mannar_DS_boundary, Mannar_GN_boundary
from .serializers import ShapeLayerSerializers, MannarDSDSerializer, MannarGNSerializer
from rest_framework.response import Response
from django.contrib.gis.geos import Point


def LayerView(request):
    transformer = ShapeLayers.objects.all()
    serializer = ShapeLayerSerializers(transformer, many=True)
    return JsonResponse(serializer.data, safe=False)


def containedDSView(request):
    lon = request.GET.get('lon', '')
    lat = request.GET.get('lat', '')


    pnt = Point(float(lon), float(lat))

    queryset = Mannar_DS_boundary.objects.filter(geom__contains=pnt)
    serializer = MannarDSDSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

def containedGNView(request):
    lon = request.GET.get('lon', '')
    lat = request.GET.get('lat', '')
    pnt = Point(float(lon), float(lat))

    queryset = Mannar_GN_boundary.objects.filter(geom__contains=pnt)
    serializer = MannarGNSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

