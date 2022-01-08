from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Layer, Incident

from leaflet.admin import LeafletGeoAdminMixin
from leaflet_admin_list.admin import LeafletAdminListMixin

class IncidentAdmin(LeafletAdminListMixin, LeafletGeoAdminMixin, admin.ModelAdmin):
    list_display=['entity',]

admin.site.register(Incident, LeafletGeoAdmin)
admin.site.register(Layer, admin.ModelAdmin) 