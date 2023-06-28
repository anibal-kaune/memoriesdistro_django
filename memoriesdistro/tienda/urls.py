from django.urls import path
from .views import index, create, read, show, edit, delete, cd, desarrollo, quienessomos, producto, login, registro, admin, crear_usuario

urlpatterns = [
    path("", index, name="index"),
    path("cd", cd, name="cd"),
    path("desarrollo", desarrollo, name="desarrollo"),
    path("quienessomos", quienessomos, name="quienessomos"),
    path("producto/<int:producto_id>", producto, name="producto"),
    path("login", login, name="login"),
    path("registro", registro, name="registro"),
    path("administrator", admin, name="admin_index"),
    path("administrator/create_user", crear_usuario, name="create_user"),
    path('create', create, name='Crear'),
    path('read', read, name='Ver'),
    path('show', show, name='Mostrar'),
    path('edit/<str:pk>', edit, name='Editar'),
    path('delete/<str:pk>', delete, name='Eliminar')
]