from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Layer, Incident, SensitiveEntity, Damage
from import_export.admin import ExportActionMixin

from leaflet.admin import LeafletGeoAdminMixin
from leaflet_admin_list.admin import LeafletAdminListMixin

class IncidentAdmin(ExportActionMixin, LeafletAdminListMixin, LeafletGeoAdminMixin, admin.ModelAdmin):
    list_display=['entity', 'damage', 'gnd_dsd', 'siviarity', 'location_ref', 'is_approved',]

admin.site.register(Incident, IncidentAdmin)
admin.site.register(Layer, admin.ModelAdmin) 
admin.site.register(SensitiveEntity, admin.ModelAdmin)
admin.site.register(Damage, admin.ModelAdmin) 