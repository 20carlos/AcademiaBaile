"""AcademiaBaile URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from Academia import views as academia_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', academia_views.index_view, name='index'),
    url(r'^login', academia_views.login_view, name = 'login'),
    url(r'^home/', academia_views.home_view, name='home'),
    url(r'^logout', academia_views.login_out, name = 'logout'),
    url(r'^lista_alumnos/', academia_views.lista_alumnos, name='lista_alumnos'),
    url(r'^lista_clases/', academia_views.lista_clases, name='lista_clases'),
    url(r'^agregar_alumno/', academia_views.agregar_alumno, name='agregar_alumno'),
    url(r'^agregar_clase/', academia_views.agregar_clase, name='agregar_clase'),
    url(r'^eliminar_clase/(?P<id_clase>[-A-Za-z0-9_]+)$', academia_views.eliminar_clase, name='eliminar_clase'),
    url(r'^eliminar_alumno/(?P<id_alumno>[-A-Za-z0-9_]+)$', academia_views.eliminar_alumno, name='eliminar_alumno'),
    url(r'^modificar_alumno/(?P<id_alumno>[-A-Za-z0-9_]+)$', academia_views.modificar_alumno, name='modificar_alumno'),
    url(r'^modificar_clase/(?P<id_clase>[-A-Za-z0-9_]+)$', academia_views.modificar_clase, name='modificar_clase'),
    url(r'^eventos/', academia_views.eventos, name='eventos'),
    url(r'^maestros/', academia_views.maestros, name='maestros'),
    url(r'^contacto/', academia_views.contacto, name='contacto'),
]
