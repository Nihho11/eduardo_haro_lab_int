from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core import serializers as ssr
from apps.owner.models import Owner
from apps.owner.forms import OwnerForm

"""
Requisito: 
    1. Crear un registro en la BD usando la ORM de Djago que contenga.
    nombre, apellido, edad, dni, pais, vigente
"""


# Create your views here.
def owner_list(request):
    # data_context = {
    #     'nombre': 'Katty Paredes',
    #     'edad': 16,
    #     'dni': 88842232,
    #     'pais': 'Perú',
    #     'vigente': False
    # }
    data_context = [{
        'nombre': 'Katty Paredes',
        'edad': 16,
        'dni': 88842232,
        'pais': 'Perú',
        'vigente': False,
        'pokemons': [
            {
                'nombre_pokemon': 'Squirtle',
                'ataques': ['Placaje', 'Pistola de Agua', 'Burbuja', 'Hidropulso']
            }
        ]
    }, {
        'nombre': 'Juan Perez',
        'edad': 23,
        'dni': 43334434,
        'pais': 'Perú',
        'vigente': True,
        'pokemons': [
            {

            }
        ]
    }, {
        'nombre': 'Leon Jimenez',
        'edad': 33,
        'dni': 66643746,
        'pais': 'Perú',
        'vigente': True,
        'pokemons': [
            {

            }
        ]
    }, {
        'nombre': 'Pedro Suarez',
        'edad': 31,
        'dni': 23456765,
        'pais': 'Perú',
        'vigente': True,
        'pokemons': [
            {

            }
        ]
    }]

    """Crear un objeto en una tabla de la BD"""
    # p = Owner(nombre="Eduardo Haro", edad=22, dni="98765432", pais="Perú", vigente=True)
    # p.save()

    data_context = Owner.objects.all()

    """Filtración de datos: .filter()"""

    # data_context = Owner.objects.filter(nombre="Margarita Tello", edad=22)

    """Filtración de datos más precisos con: __constains"""

    # data_context = Owner.objects.filter(nombre__contains="uliana")

    """Filtración de datos más precisos con: --endswith"""

    # data_context = Owner.objects.filter(nombre__endswith="ello", edad=22)

    """Para objetos individuales se usa .get"""

    # data_context = Owner.objects.get(nombre="Eduardo Haro")

    """Para ordenar: .order_by, si quieres que sea inverso en este ejemplo pones: '-nombre' """

    # data_context = Owner.objects.order_by("nombre")

    """Ordenar concatenando diferentes métodos ORM'S"""

    # data_context = Owner.objects.filter(nombre="Messi").order_by("edad")

    """Acortar datos: obtener un rago de registror para no mostrar un millon de datos"""

    # data_context = Owner.objects.all()[0:2]

    """Eliminar datos específicos .delete()"""

    # data_context = Owner.objects.get(id=3)
    # data_context.delete()

    """Actualizar varios objetos a la ves: utilizando .update()
    no hace falta empezar con data_context =, pues estamos actualizando datos, no vamos a mostrar nada"""

    # Owner.objects.filter(nombre="Messi").update(pais="Argentina")

    """Utilizando F expressions, import from djangobdmodels!!"""

    # Owner.objects.filter(edad__lte=25).update(edad=F('edad')+10)

    """Consultas complejas con objetos Q (| = or) (& = and)"""

    # query = Q(pais__startswith="Pe") | Q(pais__startswith="Es")
    # data_context = Owner.objects.filter(query, edad=35)
    # negacion: query = Q(pais__startswith="Pe") & ~Q(edad=30)
    # query = Q(pais__startswith="Pe") & Q(edad=30)
    # data_context = Owner.objects.filter(query)

    """Error de consulta con Q: no es valido"""
    query = Q(pais__startswith='Pe') | Q(pais__startswith='Es')
    # asi no va a salir, pues primero va el query:
    # data_context = Owner.objects.filter(edad=30, query)
    return render(request, 'owner/owner_list.html', context={'data': data_context})


def owner_search(request):
    query = request.GET.get('q', '')
    print("Query: {}".format(query))

    results = (
        Q(nombre__icontains=query)
    )
    data_context = Owner.objects.filter(results)
    # data_context = Owner.objects.filter(results).distinct()
    return render(request, 'owner/owner_search.html', context={'data': data_context, 'query': query})


def owner_details(request):
    """Obtiene todos los elementos de una tabla de BD"""
    owners = Owner.objects.all()
    return render(request, 'owner/owner_details.html', context={'data': owners})


def owner_create(request):
    form = OwnerForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        edad = form.cleaned_data['edad']
        pais = form.cleaned_data['pais']

        form.save()
        return redirect('owner_details')
    else:
        form = OwnerForm()

    return render(request, 'owner/owner_create.html', {'form': form})


def owner_delete(request, id_owner):
    owner = Owner.objects.get(id=id_owner)
    owner.delete()

    return redirect('owner_details')


def owner_edit(request, id_owner):
    # print('Id de owner a editar: {}'.format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    print('Datos del owner a editar: {}'.format(owner))
    form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni': owner.dni})
    if request.method == "POST":
        form = OwnerForm(request.POST, instance=owner)
    if form.is_valid():
        form.save()
        return redirect('owner_details')
    return render(request, 'owner/owner_edit.html', context={'form': form})


"""Vistas basadas en clases"""
"""ListView, CreateView, UpdateView, DeleteView"""


class OwnerList(ListView):
    model = Owner
    template_name = 'owner/owner_list_vc.html'


class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_create.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_update_vc.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerDelete(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_vc')
    template_name = 'owner/owner_confirm_delete.html'


"""Serializers, para pasar a json"""


def ListOwnerSerializer(request):
    lista_owner = ssr.serialize('json', Owner.objects.all(), fields=['nombre', 'pais', 'edad', 'dni'])

    return HttpResponse(lista_owner, content_type="application/json")