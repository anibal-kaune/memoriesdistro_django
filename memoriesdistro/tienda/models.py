from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    sku = models.IntegerField()
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='tienda/productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_usuario = models.IntegerField()

class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    correo = models.EmailField()
    password = models.CharField(max_length=100)
    
class Rol(models.Model):
    nombre = models.CharField(max_length=100)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nombres , self.correo

class Boleta(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_de_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.total, self.fecha_de_creacion

class DetalleBoleta(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.precio, self.cantidad, self.total
