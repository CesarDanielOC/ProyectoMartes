from django.shortcuts import render, redirect
from .models import Medicamento

# Create your views here.

def inicio_vistaMedicamento(request):
    losproductos = Medicamento.objects.all()
    return render(request, 'gestionarMedicamento.html', {'misproductos': losproductos})

def registrarMedicamento(request):
    id_producto = request.POST["numidproducto"]
    nombre = request.POST["txtnombre"]
    marca = request.POST["txtmarca"]
    tipo = request.POST["txttipo"]
    volumen = request.POST["numvolumen"]
    precio = request.POST["numprecio"]
    notas_olfativas = request.POST["txtnotas"]

    Medicamento.objects.create(
        id_producto=id_producto, 
        nombre=nombre, 
        marca=marca, 
        tipo=tipo, 
        volumen=volumen, 
        precio=precio, 
        notas_olfativas=notas_olfativas
    )

    return redirect('Medicamento')

def seleccionarMedicamento(request, id_producto):
    try:
        producto = Medicamento.objects.get(id_producto=id_producto)
        return render(request, "editarMedicamento.html", {"misproductos": producto})
    except Medicamento.DoesNotExist:
        return redirect('Producto')  # Redirigir si el producto no se encuentra

def editarMedicamento(request):
    if request.method == "POST":
        id_producto = request.POST.get("numidproducto")
        nombre = request.POST.get("txtnombre")
        marca = request.POST.get("txtmarca")
        tipo = request.POST.get("txttipo")
        volumen = request.POST.get("numvolumen")
        precio = request.POST.get("numprecio")
        notas_olfativas = request.POST.get("txtnotas")

        try:
            producto = Medicamento.objects.get(id_producto=id_producto)
            producto.nombre = nombre
            producto.marca = marca
            producto.tipo = tipo
            producto.volumen = volumen
            producto.precio = precio
            producto.notas_olfativas = notas_olfativas
            producto.save()
        except Medicamento.DoesNotExist:
            return redirect('Medicamento')  # O manejar el error según lo necesites

    return redirect('Medicamento')

def borrarMedicamento(request, id_producto):
    try:
        producto = Medicamento.objects.get(id_producto=id_producto)
        producto.delete()
    except Medicamento.DoesNotExist:
        pass  # No hacer nada si no existe, podrías redirigir a un mensaje de error

    return redirect('Medicamento')
