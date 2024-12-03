from django.shortcuts import render, redirect
from .models import Paciente 
from datetime import datetime

def inicio_vistaPaciente(request):
    los_pacientes = Paciente.objects.all()  # Cambiado de reseña a paciente
    return render(request, 'gestionarPaciente.html', {'mispacientes': los_pacientes})

def registrarPaciente(request):
    if request.method == 'POST':
        id_paciente = request.POST["numidpaciente"]
        nombre = request.POST["txtnombre"]
        apellidos = request.POST["txtapellidos"]
        telefono = request.POST["txttelefono"]
        fecharegistrostr = request.POST["txtfechar"]
        fecharegistro = datetime.strptime(fecharegistrostr, '%Y-%m-%d').date()
        fechanacimientostr = request.POST["txtfechan"]
        fechanacimiento = datetime.strptime(fechanacimientostr, '%Y-%m-%d').date()
        direccion = request.POST["txtdireccion"]

        guardar_paciente = Paciente.objects.create(
            id_paciente=id_paciente, 
            nombre=nombre,
            apellidos=apellidos, 
            telefono=telefono,
            fecharegistro=fecharegistro, 
            fechanacimiento=fechanacimiento,  
            direccion=direccion
        )
        return redirect('Paciente')
    return render(request, 'gestionarPaciente.html')

def seleccionarPaciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    return render(request, "editarPaciente.html", {"mispacientes": paciente})

def editarPaciente(request):
    if request.method == 'POST':
        id_paciente = request.POST["numidpaciente"]
        nombre = request.POST["txtnombre"]
        apellidos = request.POST["txtapellidos"]
        telefono = request.POST["txttelefono"]
        fecharegistro = request.POST["txtfechar"]
        fechanacimientostr= request.POST["txtfechan"]
        fechanacimiento = datetime.strptime(fechanacimientostr, '%Y-%m-%d').date()
        direccion = request.POST["txtdireccion"]
        paciente = Paciente.objects.get(id_paciente=id_paciente)

        paciente.nombre = nombre
        paciente.apellidos = apellidos
        paciente.telefono = telefono
        paciente.fecharegistro = fecharegistro
        paciente.fecha_reseña = fechanacimiento  # Guardamos la fecha correctamente formateada
        paciente.direccion = direccion
        paciente.save()

        return redirect('Paciente')

def borrarPaciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    paciente.delete()

    return redirect('Paciente')
