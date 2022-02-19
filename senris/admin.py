from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Layer, Incident, SensitiveEntity, Damage

from leaflet.admin import LeafletGeoAdminMixin
from leaflet_admin_list.admin import LeafletAdminListMixin

class IncidentAdmin(LeafletAdminListMixin, LeafletGeoAdminMixin, admin.ModelAdmin):
    list_display=['entity',]

admin.site.register(Incident, LeafletGeoAdmin)
admin.site.register(Layer, admin.ModelAdmin) 
admin.site.register(SensitiveEntity, admin.ModelAdmin)
admin.site.register(Damage, admin.ModelAdmin) 