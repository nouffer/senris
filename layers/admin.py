from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from layers.models import MannarStreamNetwork, ShapeLayers, MannarDistrictBoundary, MannarDSBoundary, MannarGNBoundary, MannarForestCover, MannarIrrigationTank, MannarLanduse, MannarNationalRoadNetwork, MannarPACover, MannarPlaces,MannarRemainingForest, MannarRiverBasin, MannarSmallIrrigationTankPoint, MannarSmallIrrigationTankPoly

admin.site.register(ShapeLayers, LeafletGeoAdmin)
admin.site.register(MannarDistrictBoundary, LeafletGeoAdmin)
admin.site.register(MannarDSBoundary, LeafletGeoAdmin)
admin.site.register(MannarGNBoundary, LeafletGeoAdmin)
admin.site.register(MannarForestCover, LeafletGeoAdmin)
admin.site.register(MannarIrrigationTank, LeafletGeoAdmin)
admin.site.register(MannarLanduse, LeafletGeoAdmin)
admin.site.register(MannarNationalRoadNetwork, LeafletGeoAdmin)
admin.site.register(MannarPACover, LeafletGeoAdmin)
admin.site.register(MannarPlaces, LeafletGeoAdmin)
admin.site.register(MannarRemainingForest, LeafletGeoAdmin)
admin.site.register(MannarRiverBasin, LeafletGeoAdmin)
admin.site.register(MannarSmallIrrigationTankPoint, LeafletGeoAdmin)
admin.site.register(MannarSmallIrrigationTankPoly, LeafletGeoAdmin)
admin.site.register(MannarStreamNetwork, LeafletGeoAdmin)

