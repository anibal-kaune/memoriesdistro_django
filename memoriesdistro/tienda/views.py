from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import UserForm, ProductoForm
from .models import Producto, Categoria, Usuario, Cliente, Boleta, DetalleBoleta
# Create your views here.

def index(request):
    productos = Producto.objects.all()
    context = {"productos" : productos,}
    return render(request, 'tienda/index.html', context)

def cd(request):
     productos = Producto.objects.all()
     context = {"productos" : productos,}
     return render(request, 'tienda/cd.html', context)

def desarrollo(request):
     return render(request, 'tienda/desarrollo.html')

def quienessomos(request):
     return render(request, 'tienda/quienesSomos.html')

def producto(request, producto_id):
     producto = Producto.objects.get(id=producto_id)
     context={'producto':producto}
     return render(request, 'tienda/producto.html', context)

def login(request):
     return render(request, 'tienda/login.html')

def registro(request):
     return render(request, 'tienda/registro.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            return redirect('admin')
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos.'
            return render(request, 'admin/login.html', {'error_message': error_message})
    
    return render(request, 'admin/administrator.html')

def admin(request):
    productos = Producto.objects.all()
    context={'productos':productos}
    return render(request, 'admin/administrator.html', context)

#CRUD
def crear_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = UserForm()
    
    return render(request, 'admin/create_user.html', {'form': form})

"""
def create(request):
    if request.method !="POST":
        productos = Producto.objects.all()
        context={'producto':productos}
        return render(request,'create.html', context)
    else:
        nombre = request.POST["nombre"]
        codigo = request.POST["codigo"]
        precio = request.POST["precio"]
        foto = request.POST["foto"]
        descripcion = request.POST["descripcion"]
        usuario = request.POST["id_usuario"]
        categoria = request.POST["categoria"]

        objCategoria = Categoria.objects.get(id_categoria = categoria)
        objUsuario = Usuario.objects.get(id_usuario = usuario)
        obj = Producto.objects.create(nombre=nombre,
                                      codigo=codigo,
                                      precio=precio,
                                      foto=foto,
                                      descripcion=descripcion,
                                      id_usuario=objUsuario,
                                      id_categoria=objCategoria)
        obj.save()
        context={'mensaje':"Datos guardados"}
        return render(request, 'admin/create.html', context)
"""

def create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = ProductoForm()
    
    return render(request, 'admin/create.html', {'form': form})

"""
def show(request,id):
    print(id)
    #buscar un elemento
    return render(request, 'show.html')
"""
    
"""
def edit(request,pk):
    if pk !="":
        #buscar un elemento
        producto= Producto.objects.get(codigo=pk)
        categoria=Categoria.objects.all()
        print(type(producto.id_categoria.categoria))
        context={'producto':producto, 'categoria':categoria}
        if producto:
                return render(request, 'edit.html', context)
        else:
                context={'mensaje_error':"Producto no encontrado"}
                return render(request, 'admin/edit.html', context)
"""
                    
def edit(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'admin/edit.html', {'form': form, 'producto': producto})


def delete(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('admin')
    
    return render(request, 'admin/delete.html', {'producto': producto})