"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from core import views as core_views #importamos la vista de core creada en ...startapp core
from portfolio import views as portfolio_views    # importamos la vista de portfolio 

from django.conf import settings    #incluimos a settings dentro de django.conf para agregar las urls de las imagenes en /media/


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', core_views.home, name='home'), # enlazamos el paquete de vistas home a los patrones urls
    path('about/', core_views.about, name='about'), #enlazamos la vista de about a about
    path('portafolio/', portfolio_views.portafolio, name='portafolio'), #enlazamos la vista de portafolio
    path("contact/", core_views.contact, name="contact"), #enlazamos la vista contacto
    path("contact/ubicame/", core_views.ubicame, name="ubicame"),  #enlazamos la vista ubicame
]


#configuracion extendida para las imagenes
if settings.DEBUG:                               #solo si está en TRUE
    from django.conf.urls.static import static      #sirve los ficheros estaticos
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)      #agregamos a urls patterns los estaticos para que los muestre al usuario