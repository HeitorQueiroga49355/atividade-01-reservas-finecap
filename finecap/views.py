from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReservaForm
from .models import Reserva


def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
            return redirect('reserva_listar')
    else:
        form = ReservaForm()

    return render(request, "finecap/form.html", {'form': form})


def reserva_listar(request):
    reservas = Reserva.objects.all()

    filter_name = request.GET.get('nome')
    filter_value = request.GET.get('valor')
    filter_quitado = request.GET.get('quitado')
    filter_data = request.GET.get('data')


    if filter_name:
            reservas = reservas.filter(nome_empresa__icontains=filter_name)

    if filter_value:
        reservas = reservas.filter(stand__valor=filter_value)

    if filter_quitado is not None:
        reservas = reservas.filter(quitado=str(filter_quitado))

    if filter_data:
            reservas = reservas.filter(data__gte=searched_date)
    context ={
        'reservas':reservas
    }
    return render(request, "finecap/reservas.html",context)


def reserva_remover(request, id):
    aluno = get_object_or_404(Reserva, id=id)
    aluno.delete()
    return redirect('reserva_listar')


def reserva_editar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)

        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'finecap/form.html', {'form': form})
