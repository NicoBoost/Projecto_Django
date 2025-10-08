from django.shortcuts import render, redirect, get_object_or_404
from .models import myapp
from .forms import ProductoForm

def index(request):
    return render(request, 'myapp/index.html')

def listar_productos(request):
    myapp = myapp.objects.all()
    return render(request, 'myapp/listar.html', {'myapp': myapp})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'myapp/crear.html', {'form': form})

def editar_producto(request, id):
    producto = get_object_or_404(myapp, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'myapp/editar.html', {'form': form, 'producto': producto})

def eliminar_producto(request, id):
    producto = get_object_or_404(myapp, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'myapp/eliminar.html', {'producto': producto})
