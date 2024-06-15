"""
URL configuration for CursosDjango project.

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
from django.contrib import admin
from django.urls import path
from contenido import views #Se importa el archivo de views.py 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='Principal'), #Ruta para la página principal del sitio.
    path('cursos/', views.cursos, name='Cursos'), #Ruta para la página de Cursos
    path('contacto/', views.contacto, name='Contacto'), #Ruta para la página que contiende el form de contacto.
    path('ejemplo2/', views.ejemplo2, name='Ejemplo'),
]
