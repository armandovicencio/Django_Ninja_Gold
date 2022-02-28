from django.urls import path
from . import views
from . import views_forms

# http://127.0.0.1:8000/usuarios/

app_name = 'usuarios'

urlpatterns = [
    path('', views.list_usuarios, name='listado' ),
    path('add/', views.add_usuarios, name='agregar' ),
    path('edit/<int:id>', views.edit_usuarios, name='editar' ),
    path('delete/<int:id>', views.delete_usuarios, name='eliminar' ),

    path('delete/<int:id>/ajax', views.delete_usuarios_api, name='eliminar_ajax' ),
    path('add/forms/', views_forms.add_usuarios_forms, name='agregar_forms' ),
    path('edit/forms/<int:id>', views_forms.edit_usuarios_forms, name='editar_forms' ),
]
