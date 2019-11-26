from django.shortcuts import render
from django.http import HttpResponse
from cliente.models import Genero

#Formulários

from .forms import GeneroForm

#Views

def index(request):

    context = {} #{"nome":"Batman"}

    return render(request, "cliente/index.html", context)

def cadastro(request):

    if request.method == "GET":
        form = GeneroForm()
        context = { 
            "form" : form,
        }
        return render(request, "cliente/cadastroGenero.html", context)
    
    elif request.method == "POST":
    
        form = GeneroForm( request.POST )
        form.save()

        context = { 
            "sucesso" : "Gênero cadastrado com sucesso",
        }

        return render(request, "cliente/cadastroGenero.html", context)
    
    else: 
        return HttpResponse("<h2>Tá errado issaí</h2>")


def busca(request, cliente=0):

    busca = Genero.objects.all()

    context= {
        "generos":busca,
    }

    return render(request, "cliente/buscaGenero.html", context)