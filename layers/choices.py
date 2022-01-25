from django.utils.translation import gettext_lazy as _

LAYER_CHOICES = (
    (1, _("Mannar_District_boundary")),
    (2, _("Mannar_DS_boundary")),
    (3, _("Mannar_GN_boundary")),
    (4, _("Mannar_Declared_forest")),
    (5, _("Mannar_Forest_cover")),
    (6, _("Mannar_Landuse")),
    (7, _("Mannar_Major_irr_tank")),
    (8, _("Mannar_Other_state_forest")),
    (9, _("Mannar_PA_cover")),
    (10, _("Mannar_Place")),
    (11, _("Mannar_River_basin_boundary")),
    (12, _("Mannar_River_stream")),
    (13, _("Mannar_Road")),
    (14, _("Mannar_Slope")),
    (15, _("Mannar_Small_irr_tank")),
    (16, _("Ampara_Declared_forest")),
    (17, _("Ampara_Disrict_boundary")),
    (18, _("Ampara_DS_boundary")),
    (19, _("Ampara_Forest_cover")),
    (20, _("Ampara_GN_boundary")),
    (21, _("Ampara_Landuse")),
    (22, _("Ampara_Major_irr_tank")),
    (23, _("Ampara_Other_state_forest")),
    (24, _("Ampara_Place")),
    (25, _("Ampara_River_basin_boundary")),
    (26, _("Ampara_River_stream")),
    (27, _("Ampara_Road")),
    (28, _("Ampara_Slope")),
    (29, _("Ampara_Small_irr_tank"))
)
RELEVANCE_CHOICES = (
    (1, _("Unread")),
    (2, _("Read"))
)