from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm  # lo crearemos abajo

# Página principal / menú
def index(request):
    return render(request, 'myapp/index.html')

# Listar productos
def listar_productos(request):
    lista_productos = Producto.objects.all()
    return render(request, 'myapp/listar.html', {'productos': lista_productos})

# Crear nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'myapp/crear.html', {'form': form})

# Editar producto
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'myapp/editar.html', {'form': form})

# Eliminar producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'myapp/eliminar.html', {'producto': producto})
