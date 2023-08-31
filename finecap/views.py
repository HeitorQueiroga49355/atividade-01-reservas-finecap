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
    context = {
        'reservas': reservas
    }
    return render(request, "finecap/reservas.html", context)

def reserva_remover(request, id):
    aluno = get_object_or_404(Reserva, id=id)
    aluno.delete()
    return redirect('reserva_listar')

def reserva_editar(request,id):
    aluno = get_object_or_404(Reserva,id=id)
   
    if request.method == 'POST':
        form = ReservaForm(request.POST,instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
    else:
        form = ReservaForm(instance=aluno)

    return render(request,'finecap/form.html',{'form':form})

