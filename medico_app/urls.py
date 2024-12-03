from django.urls import path
from medico_app import views

urlpatterns = [
    path('Medico',views.inicio_vistaMedico,name="Medico"),
    path("registrarMedico/",views.registrarMedico,name="registrarMedico"),
    path("seleccionarMedico/<id_proveedor>",views.seleccionarMedico,name="seleccionarMedico"),
    path("editarMedico/",views.editarMedico,name="editarMedico"),
    path("borrarMedico/<id_proveedor>",views.borrarMedico,name="borrarMedico")
]