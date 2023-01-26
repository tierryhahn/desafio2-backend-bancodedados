from django.db import models
import uuid

class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    tipo = models.CharField(max_length=1)
    data = models.CharField(max_length=10)
    valor = models.FloatField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=15)
    dono_da_loja = models.CharField(max_length=15)
    nome_loja = models.CharField(max_length=20)

class FileForm(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    data = models.DateTimeField(auto_now_add=True)
    File = models.FileField()
