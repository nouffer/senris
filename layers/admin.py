from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import \
    Mannar_Declared_forest, \
    Mannar_District_boundary, \
    Mannar_DS_boundary, \
    Mannar_Forest_cover, \
    Mannar_GN_boundary, \
    Mannar_Landuse, \
    Mannar_Major_irr_tank, \
    Mannar_Other_state_forest, \
    Mannar_PA_cover, \
    Mannar_Place, \
    Mannar_River_basin_boundary, \
    Mannar_River_stream, \
    Mannar_Road, \
    Mannar_Slope, \
    Mannar_Small_irr_tank,\
    Ampara_Declared_forest, \
    Ampara_Disrict_boundary, \
    Ampara_DS_boundary, \
    Ampara_Forest_cover, \
    Ampara_GN_boundary,\
    Ampara_Landuse, \
    Ampara_Major_irr_tank, \
    Ampara_Other_state_forest, \
    Ampara_Place, \
    Ampara_River_basin_boundary, \
    Ampara_River_stream, \
    Ampara_Road, \
    Ampara_Slope, \
    Ampara_Small_irr_tank, \
    ShapeLayers

admin.site.register(ShapeLayers, LeafletGeoAdmin)
admin.site.register(Ampara_Small_irr_tank, LeafletGeoAdmin)
admin.site.register(Ampara_Slope, LeafletGeoAdmin)
admin.site.register(Ampara_Road, LeafletGeoAdmin)
admin.site.register(Ampara_River_stream, LeafletGeoAdmin)
admin.site.register(Ampara_River_basin_boundary, LeafletGeoAdmin)
admin.site.register(Ampara_Place, LeafletGeoAdmin)
admin.site.register(Ampara_Other_state_forest, LeafletGeoAdmin)
admin.site.register(Ampara_Major_irr_tank, LeafletGeoAdmin)
admin.site.register(Ampara_Landuse, LeafletGeoAdmin)
admin.site.register(Ampara_GN_boundary, LeafletGeoAdmin)
admin.site.register(Ampara_Forest_cover, LeafletGeoAdmin)
admin.site.register(Ampara_DS_boundary, LeafletGeoAdmin)
admin.site.register(Ampara_Disrict_boundary, LeafletGeoAdmin)
admin.site.register(Ampara_Declared_forest, LeafletGeoAdmin)
admin.site.register(Mannar_Small_irr_tank, LeafletGeoAdmin)
admin.site.register(Mannar_Slope, LeafletGeoAdmin)
admin.site.register(Mannar_Road, LeafletGeoAdmin)
admin.site.register(Mannar_River_stream, LeafletGeoAdmin)
admin.site.register(Mannar_River_basin_boundary, LeafletGeoAdmin)
admin.site.register(Mannar_Place, LeafletGeoAdmin)
admin.site.register(Mannar_PA_cover, LeafletGeoAdmin)
admin.site.register(Mannar_Other_state_forest, LeafletGeoAdmin)
admin.site.register(Mannar_Major_irr_tank, LeafletGeoAdmin)
admin.site.register(Mannar_Landuse, LeafletGeoAdmin)
admin.site.register(Mannar_GN_boundary, LeafletGeoAdmin)
admin.site.register(Mannar_Forest_cover, LeafletGeoAdmin)
admin.site.register(Mannar_DS_boundary, LeafletGeoAdmin)
admin.site.register(Mannar_District_boundary, LeafletGeoAdmin)
admin.site.register(Mannar_Declared_forest, LeafletGeoAdmin)

