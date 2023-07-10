from django import forms
from django.contrib.auth.models import User
from .models import Producto, Usuario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('sku', 'nombre', 'precio', 'descripcion', 'foto', 'categoria', 'id_usuario')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nombres', 'correo', 'password')