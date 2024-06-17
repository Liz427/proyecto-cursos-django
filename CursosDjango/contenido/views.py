from django.shortcuts import render, HttpResponse

# Create your views here.

#Función Principal para mostrar la bienvenida.
def principal(request):
    return render(request, 'contenido/principal.html')

#Función Cursos para mostrar los cursos impartidos.
def cursos(request):
    return render(request, 'contenido/cursos.html')

#Función contacto para solicitar info sobre un curso en específico.
def contacto(request):
    return render(request, 'contenido/contacto.html')


def ejemplo2(request):
    return render(request, 'contenido/ejemplo2.html')