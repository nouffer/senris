from django.db.models import base
from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import IncidentViewSet, IndexView, DamageViewSet, SensitiveEntityViewSet, RegistrationAPI, LoginAPI
from django.urls import path, include
from knox import views as knox_views
from django.contrib import admin


router = DefaultRouter()

router.register(prefix='v1/incidents', viewset=IncidentViewSet, basename='incident')
router.register(prefix='v1/damage', viewset=DamageViewSet, basename='damage')
router.register(prefix='v1/entity', viewset=SensitiveEntityViewSet, basename='entity')

urlpatterns = router.urls

urlpatterns += [
    path('layers/', include("layers.urls")),
    path('auth/', include('knox.urls'))
]