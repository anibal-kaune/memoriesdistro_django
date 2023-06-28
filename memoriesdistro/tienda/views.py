from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserForm, ProductoForm
from .models import Producto, Categoria, Usuario, Cliente, Boleta, DetalleBoleta
# Create your views here.

def index(request):
    productos = Producto.objects.all()
    context = {"productos" : productos,}
    return render(request, 'tienda/index.html', context)

def cd(request):
     return render(request, 'tienda/cd.html')

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

#CRUD
def crear_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    else:
        form = UserForm()
    
    return render(request, 'admin/create_user.html', {'form': form})

def create(request):
    if request.method is not "POST":
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
        return render(request, 'create.html', context)

def admin(request):
    productos = Producto.objects.all()
    context={'productos':productos}
    return render(request, 'admin/administrator.html', context)

def show(request,id):
    print(id)
    #buscar un elemento
    return render(request, 'show.html')

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
                return render(request, 'read.html', context)
    

def delete(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('Ver')
    
    return render(request, 'tienda/delete.html', {'producto': producto})