from django.urls import path
from citas_app import views

urlpatterns = [
    path('Citas',views.inicio_vistaCitas,name="Citas"),
    path("registrarCitas/",views.registrarCitas,name="registrarCitas"),
    path("seleccionarCitas/<id_promocion>",views.seleccionarCitas,name="seleccionarCitas"),
    path("editarCitas/",views.editarCitas,name="editarCitas"),
    path("borrarCitas/<id_promocion>",views.borrarCitas,name="borrarCitas")
]