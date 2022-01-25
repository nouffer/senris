from django.urls import path, include


from .views import LayerView


urlpatterns = [
    path('', LayerView, name="layers"),
]
