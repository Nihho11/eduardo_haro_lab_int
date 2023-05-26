from django.shortcuts import render


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

    return render(request, 'owner/owner_list.html', context={'data': data_context})


"""
Requerimientos:
1. El mensaje en la plantilla debe decir: "Nombre" es "mayor/menor" de edad  y de nacionalidad "País
2. Segundo mensaje será: Su pase está vigente
"""
