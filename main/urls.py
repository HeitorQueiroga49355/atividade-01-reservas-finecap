from django.contrib import admin
from django.urls import path
from aluno.views import index
from finecap.views import reserva_criar, reserva_listar, reserva_remover, reserva_editar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('reserva/',reserva_criar,name='reserva_criar'),
    path('reserva/listar',reserva_listar,name='reserva_listar'),
    path('reserva/remover/<int:id>/', reserva_remover, name='reserva_remover'),
    path('reserva/editar/<int:id>/',reserva_editar, name='reserva_editar')
]

"""path('aluno/editar/<int:id>/',aluno_editar, name='aluno_editar'),
path('aluno/remover/<int:id>/',aluno_remover,name='aluno_remover'),
path('aluno/listar',aluno_listar,name='aluno_listar'), """
