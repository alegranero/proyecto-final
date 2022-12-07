from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, FamiliarForm # <-- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return  render(request, 
    'ejemplo/saludar_a.html',
    {'nombre': nombre}
    )

def sumar(request, a, b):
    return render(request,
    'ejemplo/sumar.html',
    {'a': a,
    'b': b,
    'resultado': a+b
    }
    )

def buscar(request):
    lista_de_nombre = ['Alejo','Matias','Marcelo']
    query = request.GET['q'] #GET en sí mismo es un diccionario - podemos acceder a la variable query
    if query in lista_de_nombre:
        indice_de_resultado = lista_de_nombre.index(query)
        resultado = lista_de_nombre[indice_de_resultado]
    else:
        resultado = 'no hay match'
    return render(request, 'ejemplo/buscar.html',{'resultado': resultado})

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def division(request, c, d):
    return render(request,
    'ejemplo/division.html',
    {'c': c,
    'd': d,
    'resultado': c/d
    }
    )

class BuscarFamiliar(View): #View sirve para permitir "get" y "post", es una clase heredada
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        return render(request, self.template_name, {"form": form})
        