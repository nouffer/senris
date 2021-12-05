from django.core.serializers import serialize
from django.shortcuts import render
from .models import Layer, Incident, District
from rest_framework import viewsets
from .serializers import IncidentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



def IndexView(request):
    lyr = Layer.objects.all()
    dist = District.objects.all();
    return render(request, 'senris/index.html', {'wms_layers': lyr, 'district': dist})


class IncidentViewSet(viewsets.ModelViewSet):
    queryset=Incident.objects.all()
    serializer_class=IncidentSerializer

    def get_queryset(self):
        dist = self.request.GET.get('dist')
        if dist != None :
            queryset = Incident.objects.filter(district=dist)
        else:
            queryset = Incident.objects.all()
        return queryset

