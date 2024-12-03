from django.shortcuts import render, redirect
from .models import Receta

def inicio_vistaReceta(request):
    lospedidos = Receta.objects.all()
    return render(request, 'gestionarReceta.html', {'mispedidos': lospedidos})

def registrarReceta(request):
    id_pedido = request.POST["numidpedido"]
    id_cliente = request.POST["numidcliente"]
    fecha_receta = request.POST["txtfechareceta"]
    total_pedido = request.POST["txttotalpedido"]
    estado_pedido = request.POST["txtestadopedido"]
    metodo_pago = request.POST["txtmetodopago"]
    direccion_envio = request.POST["txtdireccionenvio"]

    guardarpedido = Receta.objects.create(id_pedido=id_pedido, id_cliente=id_cliente, fecha_receta=fecha_receta,total_pedido=total_pedido, estado_pedido=estado_pedido,metodo_pago=metodo_pago, direccion_envio=direccion_envio)

    return redirect('Receta')

def seleccionarReceta(request, id_pedido):
    Pedido_ = Receta.objects.get(id_pedido=id_pedido)
    return render(request, "editarReceta.html", {"misPedido": Pedido_})

def editarReceta(request):
    id_pedido = request.POST.get("numidpedido")
    id_cliente = request.POST.get("numidcliente")
    fecha_receta = request.POST.get("txtfechareceta")
    total_pedido = request.POST.get("txttotalpedido")
    estado_pedido = request.POST.get("txtestadopedido")
    metodo_pago = request.POST.get("txtmetodopago")
    direccion_envio = request.POST.get("txtdireccionenvio")

    Pedido_ = Receta.objects.get(id_pedido=id_pedido)

    Pedido_.id_cliente = id_cliente
    Pedido_.fecha_receta = fecha_receta
    Pedido_.total_pedido = total_pedido
    Pedido_.estado_pedido = estado_pedido
    Pedido_.metodo_pago = metodo_pago
    Pedido_.direccion_envio = direccion_envio
    Pedido_.save()

    return redirect('Receta')

def borrarReceta(request, id_pedido):
    Pedido_ = Receta.objects.get(id_pedido=id_pedido)
    Pedido_.delete()

    return redirect('Receta')
