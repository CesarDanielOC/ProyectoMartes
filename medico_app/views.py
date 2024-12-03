from django.shortcuts import render, redirect
from .models import Medico

# Create your views here.

def inicio_vistaMedico(request):
    lasproveedor=Medico.objects.all()
    return render(request,'gestionarMedico.html',{'misproveedor':lasproveedor})

def registrarMedico(request):
    id_proveedor=request.POST["numidproveedor"]
    nombre_empresa=request.POST["txtnombreempresa"]
    contacto=request.POST["txtcontacto"]
    telefono=request.POST["numtelefono"]
    correo_electronico=request.POST["txtcorreoelectronico"]
    direccion=request.POST["txtdireccion"]
    fechadecontratacion=request.POST["txtfechac"]


    guardarproveedor=Medico.objects.create(id_proveedor=id_proveedor,nombre_empresa=nombre_empresa,contacto=contacto,telefono=telefono,correo_electronico=correo_electronico,direccion=direccion,fechadecontratacion=fechadecontratacion)

    return redirect('Medico')

def seleccionarMedico(request,id_proveedor):
    proveedor=Medico.objects.get(id_proveedor=id_proveedor)
    return render(request,"editarMedico.html",{"misproveedor":proveedor})

def editarMedico(request):
    id_proveedor=request.POST["numidproveedor"]
    nombre_empresa=request.POST["txtnombreempresa"]
    contacto=request.POST["txtcontacto"] 
    telefono=request.POST["numtelefono"]
    correo_electronico=request.POST["txtcorreoelectronico"]
    direccion=request.POST["txtdireccion"]
    fechadecontratacion=request.POST["txfechac"]


    proveedor=Medico.objects.get(id_proveedor=id_proveedor)

    proveedor.nombre_empresa=nombre_empresa
    proveedor.contacto=contacto
    proveedor.telefono=telefono
    proveedor.correo_electronico=correo_electronico
    proveedor.direccion=direccion
    proveedor.fechadecontratacion=fechadecontratacion
    proveedor.save()

    return redirect('Medico')

def borrarMedico(request,id_proveedor):
    proveedor=Medico.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()

    return redirect('Medico')