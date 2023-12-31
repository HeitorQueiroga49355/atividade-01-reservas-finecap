from django.db import models


class Stand(models.Model):
    localizacao = models.CharField(max_length=255)
    valor = models.FloatField()

    def __str__(self):
        return self.localizacao


class Reserva(models.Model):
    cnpj = models.CharField(max_length=12)
    nome_empresa = models.TextField()
    categoria_empresa = models.CharField(max_length=50)
    quitado = models.BooleanField()
    stand = models.OneToOneField(Stand, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.nome_empresa

