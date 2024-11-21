from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.

def home(request): 
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    varnome = request.POST.get("nome")
    Pessoa.objects.create(nome=varnome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id): 
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def update(request, id):
    novoNome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = novoNome
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect (home)