from django.shortcuts import render
from .models import Project             # se carga la clase Project desde models para recuperar los proyectos creados

# Create your views here.

#definimos la funcion Portafolio
def portafolio(request):
    projects=Project.objects.all()    # se crea una lista de proyectos llamada projects, se hace referencia a la clase Project dentro una lista de lista interna llamada objects que gestiona en tiempo de ejecución cada modelo, all devuelve todos los objetos que tiene el modelo de proyecto
    return render(request, 'portfolio/portafolio.html', {'projects':projects})      #se inyecta una lista de proyectos en el template {diccionario de contexto}