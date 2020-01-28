from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Balance, Movimiento, Categoria
from .forms import MovimientoForm


# Create your views here.

def getBadget(request):
    balance= Balance.objects.all()
    movimiento = Movimiento.objects.all()
    return render(request, 'home.html', {"balance" : balance, "movimiento" : movimiento })

def Movement(request):
    template_name ='crear_movimiento.html'
    form = MovimientoForm()

    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            print("si es valido")
            form.save()
            #se afecta el balance
            balance = Balance.objects.get(pk=1)
            if request.POST['tipo']  == 'Gasto': #gasto
                balance.saldo -= int(request.POST['monto'])
                balance.gastos += int(request.POST['monto'])
            else:
                balance.saldo += int(request.POST['monto'])
                balance.ingresos += int(request.POST['monto'])
            balance.save()

            return HttpResponseRedirect('/')

    return render(request, template_name, {'form': form})