"""senris_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from senris.views import IndexView, RegistrationAPI, LoginAPI
from knox import views as knox_views


from senris.views import IndexView, DefaulttView, RegistrationAPI, LoginAPI, UserAPI, privacyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DefaulttView, name="index"),
    path('privacy/', privacyView, name="privacy"),
    path('incidents/', IndexView, name="incidents"),
    path("accounts/", include("django.contrib.auth.urls")), 
    path('api/', include("senris.urls")),
    path('layers/', include("layers.urls")),
    path('login/', LoginAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('register/', RegistrationAPI.as_view()),
    path('user/', UserAPI.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "SENRIS Admin"
admin.site.site_title = "SENRIS GIS Admin Portal"
admin.site.index_title = "Welcome to SENRIS GIS Portal"