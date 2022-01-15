from django.utils.translation import gettext_lazy as _

LAYER_CHOICES = (
    (1, _("Mannar District boundary")),
    (2, _("Mannar DS Boundary")),
    (3, _("Mannar GN boundary")),
    (4, _("Mannar Forestcover")),
    (5, _("Mannar irrigation tank")),
    (6, _("Mannar Landuse")),
    (7, _("Mannar Roads")),
    (8, _("Mannar PACover")),
    (9, _("Mannar Places")),
    (10, _("Mannar Remaining Forest")),
    (11, _("Mannar River basin")),
    (12, _("Mannar Small Irrigation Tanks Point")),
    (13, _("Mannar Small Irrigation Tanks Polygon")),
    (14, _("Mannar Stream Network"))
)
RELEVANCE_CHOICES = (
    (1, _("Unread")),
    (2, _("Read"))
)