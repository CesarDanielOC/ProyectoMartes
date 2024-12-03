from django.urls import path
from paciente_app import views

urlpatterns = [
    path('', views.inicio_vistaPaciente, name="Paciente"),
    path("registrarPaciente/", views.registrarPaciente, name="registrarPaciente"),
    path("seleccionarPaciente/<id_paciente>", views.seleccionarPaciente, name="seleccionarPaciente"),
    path("editarPaciente/", views.editarPaciente, name="editarPaciente"),
    path("borrarPaciente/<id_paciente>", views.borrarPaciente, name="borrarPaciente"),
]
