from django.shortcuts import render
from .models import Animal
from .models import Colaborador
from .models import Protectora

# Create your views here.
def animal_list(request):
    animales = Animal.objects.all()  # Obtener todos los animales
    return render(request, 'animal_list.html', {'animales': animales})

def protectora_list(request):
    protectoras = Protectora.objects.all()  # Obtener todas las protectoras
    return render(request, 'protectora_list.html', {'protectoras': protectoras})

def colaborador_list(request):
    colaboradores = Colaborador.objects.all()  # Obtener todos los colaboradores
    return render(request, 'colaborador_list.html', {'colaboradores': colaboradores})
