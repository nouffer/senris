from django.urls import path, include


from .views import LayerView, containedDSView, containedGNView


urlpatterns = [
    path('', LayerView, name="layers"),
    path('contained_ds/', containedDSView, name="containedds"),
    path('contained_gn/', containedGNView, name="containedgn"),
]
