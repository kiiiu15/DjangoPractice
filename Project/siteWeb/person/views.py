from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    var = "Texto de prueba para ver que se puede imprimir desde pyhton"
    return render(request, 'person/index.html', {
        'var': var
    })


def getById(request, idPerson):
    return HttpResponse("Accediste a person: %s" % idPerson)
