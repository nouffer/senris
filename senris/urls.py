from django.db.models import base
from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import IncidentViewSet, IndexView
from django.urls import path

router = DefaultRouter()

router.register(prefix='v1/incidents', viewset=IncidentViewSet, basename='incident')

urlpatterns = router.urls