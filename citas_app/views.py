from django.shortcuts import render, redirect
from .models import Citas

# Create your views here.

def inicio_vistaCitas(request):
    laspromocion=Citas.objects.all()
    return render(request,'gestionarCitas.html',{'mispromocion':laspromocion})

def registrarCitas(request):
    id_promocion=request.POST["numidpromocion"]
    descripcion=request.POST["txtdescripcion"]
    fecha_inicio=request.POST["txtfechainicio"]
    fecha_fin=request.POST["txtfechafin"]
    descuento=request.POST["numdescuento"]
    productos_aplicados=request.POST["numproductosaplicados"]
    condiciones=request.POST["txtcondiciones"]

    guardarpromocion=Citas.objects.create(id_promocion=id_promocion,descripcion=descripcion,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,descuento=descuento,productos_aplicados=productos_aplicados,condiciones=condiciones)

    return redirect('Citas')

def seleccionarCitas(request,id_promocion):
    promocion=Citas.objects.get(id_promocion=id_promocion)
    return render(request,"editarCitas.html",{"mispromocion":promocion})

def editarCitas(request):
    id_promocion=request.POST["numidpromocion"]
    descripcion=request.POST["txtdescripcion"]
    fecha_inicio=request.POST["txtfechainicio"] 
    fecha_fin=request.POST["txtfechafin"]
    descuento=request.POST["numdescuento"]
    productos_aplicados=request.POST["txtproductosaplicados"]
    condiciones=request.POST["txtcondiciones"]

    promocion=Citas.objects.get(id_promocion=id_promocion)

    promocion.descripcion=descripcion
    promocion.fecha_inicio=fecha_inicio
    promocion.fecha_fin=fecha_fin
    promocion.descuento=descuento
    promocion.productos_aplicados=productos_aplicados
    promocion.condiciones=condiciones
    promocion.save()

    return redirect('Citas')

def borrarCitas(request,id_promocion):
    promocion=Citas.objects.get(id_promocion=id_promocion)
    promocion.delete()

    return redirect('Citas')