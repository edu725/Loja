from django.shortcuts import redirect, render
from myapp.models import  *
from myapp.forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    x = Roupa.objects.all()
    return render(request, 'myapp/index.html', {'itens': x})

def create(request):
    form =  RoupaForm
    if request.method == "POST":
        form = RoupaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, "myapp/create.html", {"forms":form})



def edit(request, id):
    item =  Roupa.objects.get(pk=id)
    form =  RoupaForm(instance=item)
    return render(request, "myapp/update.html",{"form":form, "item":item})


def update(request, id):
    try:
        if request.method == "POST":
            item =  Roupa.objects.get(pk=id)
            form = RoupaForm(request.POST, request.FILES, instance=item)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            

def read(request, id):
    item =  Roupa.objects.get(pk=id)
    return render(request, "myapp/read.html", {"item":item})

def delete(request, id):
    item =  Roupa.objects.get(pk=id)
    item.delete()
    messages.success(request, 'item foi deletada com sucesso!')
    return redirect('index')
