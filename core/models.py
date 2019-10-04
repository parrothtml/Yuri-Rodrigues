from django.db import models

class Pessoa(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(max_length=255, blank=False, null=False)
    contato = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome

class Cliente(Pessoa):
    renda = models.DecimalField(max_digits=5, decimal_places=2)
    credito = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField()

class Fornecedor(Pessoa):
    nome_fantasia = models.CharField(max_length=255, blank=False, null=False)
    cnpj = models.CharField(max_length=14, blank=False, null=False)
