from django.shortcuts import render, get_object_or_404

from .models import Person


# Create your views here.


def index(request):
    var = "Texto de prueba para ver que se puede imprimir desde pyhton"
    return render(request, 'person/index.html', {
        'var': var
    })


def getById(request, idPerson):

    person = get_object_or_404(Person, pk=idPerson)
    return render(request,'person/personDetail.html', {'person': person})
