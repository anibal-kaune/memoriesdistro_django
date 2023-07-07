from django.urls import path
from .views import index, create, edit, delete, cd, desarrollo, quienessomos, producto, login, registro, admin, crear_usuario
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", index, name="index"),
    path("cd", cd, name="cd"),
    path("desarrollo", desarrollo, name="desarrollo"),
    path("quienessomos", quienessomos, name="quienessomos"),
    path("producto/<int:producto_id>", producto, name="producto"),
    path("login", login, name="login"),
    path("registro", registro, name="registro"),
    path("administrator", admin, name="admin"),
    path("administrator/create_user", crear_usuario, name="create_user"),
    path('create', create, name='Crear'),
    #path('show', show, name='Mostrar'),
    path('edit/<str:producto_id>', edit, name='Editar'),
    path('delete/<str:producto_id>', delete, name='Eliminar')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)