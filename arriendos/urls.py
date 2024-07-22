"""
URL configuration for arriendos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from inmuebles import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.register, name="register"),
    path("", views.home, name="home"),
    path("agregar/", views.agregar_inmueble, name="agregar_inmueble"),
    path("listar/", views.listar_inmuebles, name="listar_inmuebles"),
    path("editar/<int:pk>/", views.editar_inmueble, name="editar_inmueble"),
    path("eliminar/<int:pk>/", views.eliminar_inmueble, name="eliminar_inmueble"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
