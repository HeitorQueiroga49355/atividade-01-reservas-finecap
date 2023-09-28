from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReservaForm
from .models import Reserva
from django.core.paginator import Paginator


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
    page_number = request.GET.get("page")

    if filter_name:
            reservas = reservas.filter(nome_empresa__icontains=filter_name)

    if filter_value:
        reservas = reservas.filter(stand__valor=filter_value)

    if filter_quitado is not None:
        reservas = reservas.filter(quitado=str(filter_quitado))

    if filter_data:
            reservas = reservas.filter(data__gte=filter_data)
    
    paginator = Paginator(reservas, 5)
    page_obj = paginator.get_page(page_number)

    context ={
        'reservas':page_obj,
        'has_next': page_obj.has_next,
        'has_previous': page_obj.has_previous
    }
    if (page_number == None or page_number == ''):
        context['next_page'] = '2'
    else:
        context['next_page'] = str(int(page_number) + 1)
        context['previous_page'] = str(int(page_number) - 1)
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
