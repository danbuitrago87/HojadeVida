from django.shortcuts import render, HttpResponse
# Create your views here.
#definimos la funcion home para la vista a través del requerimiento del cliente y retornamos respuesta html
def home(request):
    return render (request, 'core/home.html')

#definimos la funcion acerca de... para la vista a través del requerimiento del cliente y retornamos respuesta html (con HttpResponse(codigo html)) con render no es necesario escribir código html aqui sino en templates
def about(request):
    return render(request, 'core/about.html')

#definimos la vista de contacto
def contact(request):
    return render(request, 'core/contact.html')

def ubicame(request):
    return render(request,'core/ubicame.html')