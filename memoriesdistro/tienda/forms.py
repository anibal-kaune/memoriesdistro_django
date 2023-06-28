from django import forms
from django.contrib.auth.models import User
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'descripcion', 'foto', 'categoria', 'id_usuario')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')