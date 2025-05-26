from django.db import models
from PIL import Image

# Create your models here.
class Fabricante(models.Model):
    nome = models.CharField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome

class Item(models.Model):
    fabricante = models.ForeignKey('Fabricante', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    partnumber = models.CharField(max_length=50, unique=True,)
    img = models.ImageField(upload_to='itens/')
    quantidade = models.PositiveIntegerField(default=0)
    endereco = models.CharField(max_length=50, unique=True, null=False, blank=False)
    disponivel = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} ({self.fabricante}) - {self.quantidade} unidades - {'Disponível' if self.disponivel else 'Indisponível'}"

    def save(self, *args, **kwargs):
        self.disponivel = self.quantidade > 0
        super().save(*args, **kwargs)
        