from django.shortcuts import render, redirect
from .database import medicamentos

import unicodedata

def quitar_tildes(texto):
    #Separa las letras de sus tildes y luego elimina las marcas de acento para que la búsqueda sea más flexible
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def index(request):
    query = request.GET.get('q', '').strip()
    if query:
        #Convierte todo a minúsculas y quita las tildes tanto de la búsqueda como del nombre del medicamento
        query_norm = quitar_tildes(query.lower())
        resultados = [m for m in medicamentos if query_norm in quitar_tildes(m['nombre'].lower())]
    else:
        resultados = medicamentos
    return render(request, 'farmacy/index.html', {
        'medicamentos': resultados,
        'total': len(medicamentos),
        'query': query,
    })

def login_view(request):
    error = None
    if request.method == 'POST':
        user = request.POST.get('username')
        passw = request.POST.get('password')
        if user == 'admin' and passw == 'admin123':
            return redirect('index')
        else:
            error = "Usuario o contraseña incorrectos"
    return render(request, 'farmacy/login.html', {'error': error})