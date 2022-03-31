from django.core.serializers import serialize
from django.shortcuts import render
from .models import Layer, Incident, Damage, SensitiveEntity
from rest_framework import viewsets
from .serializers import IncidentSerializer, DamageSerializer, SensitiveEntitySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from layers.models import ShapeLayers
from rest_framework.parsers import JSONParser, MultiPartParser



def IndexView(request):
    lyr = Layer.objects.all()
    shapeLayers =  ShapeLayers.objects.all()
    entities = SensitiveEntity.objects.all()
    return render(request, 'senris/index.html', {'wms_layers': lyr, 'md': shapeLayers, 'entities':entities})

def DefaulttView(request):

    return render(request, 'senris/default.html')


class IncidentViewSet(viewsets.ModelViewSet):
    queryset=Incident.objects.all()
    serializer_class=IncidentSerializer
    # parser_classes = (MultiPartParser, JSONParser)

    def get_queryset(self):
        dist = self.request.GET.get('dist')
        if dist != None :
            queryset = Incident.objects.filter(entity=dist)
        else:
            queryset = Incident.objects.all()
        return queryset


class DamageViewSet(viewsets.ModelViewSet):
    queryset=Damage.objects.all()
    serializer_class=DamageSerializer

class SensitiveEntityViewSet(viewsets.ModelViewSet):
    queryset=SensitiveEntity.objects.all()
    serializer_class=SensitiveEntitySerializer