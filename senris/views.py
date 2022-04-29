from django.core.serializers import serialize
from django.shortcuts import render
from .models import Layer, Incident, Damage, SensitiveEntity
from rest_framework import viewsets
from knox.models import AuthToken
from .serializers import IncidentSerializer, DamageSerializer, SensitiveEntitySerializer, CreateUserSerializer, UserSerializer, LoginUserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from layers.models import ShapeLayers
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics



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
            queryset = Incident.objects.filter(entity=dist, is_approved=True)
        else:
            queryset = Incident.objects.filter(is_approved=True)
        return queryset


class DamageViewSet(viewsets.ModelViewSet):
    queryset=Damage.objects.all()
    serializer_class=DamageSerializer

class SensitiveEntityViewSet(viewsets.ModelViewSet):
    queryset=SensitiveEntity.objects.all()
    serializer_class=SensitiveEntitySerializer


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user