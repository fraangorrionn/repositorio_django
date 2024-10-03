from django.contrib import admin

# Register your models here.
from .models import Animal
admin.site.register(Animal)

from .models import Colaborador
admin.site.register(Colaborador)
 
from .models import Protectora
admin.site.register(Protectora)