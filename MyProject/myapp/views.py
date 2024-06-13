from django.shortcuts import redirect, render
from myapp.models import  *
from myapp.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    x = Livro.objects.all()
    return render(request, 'myapp/index.html', {'itens': x})

def spa(request):
    y = Livro.objects.all()
    return render(request, 'spa/spa.html', {'itens': y})

def create(request):
    form =  LivroForm
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, "myapp/create.html", {"forms":form})



def edit(request, id):
    item =  Livro.objects.get(pk=id)
    form =  LivroForm(instance=item)
    return render(request, "myapp/update.html",{"form":form, "item":item})


def update(request, id):
    try:
        if request.method == "POST":
            item =  Livro.objects.get(pk=id)
            form = LivroForm(request.POST, request.FILES, instance=item)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            

def read(request, id):
    item =  Livro.objects.get(pk=id)
    return render(request, "myapp/read.html", {"item":item})

def delete(request, id):
    item =  Livro.objects.get(pk=id)
    item.delete()
    messages.success(request, 'item foi deletada com sucesso!')
    return redirect('index')


