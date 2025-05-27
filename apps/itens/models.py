from django.db import models
from PIL import Image

# Create your models here.
class Fabricante(models.Model):
    nome_do_fabricante = models.CharField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome_do_fabricante

class Item(models.Model):

    fabricante = models.ForeignKey('Fabricante', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    partnumber = models.CharField(max_length=50, unique=True,)
    img = models.ImageField(upload_to='itens/')
    quantidade = models.PositiveIntegerField(default=0)
    endereco = models.CharField(max_length=50, unique=True, null=False, blank=False)
    disponivel = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    def __str__(self):
        return f"{self.nome} ({self.fabricante}) - {self.quantidade} unidades - {'Disponível' if self.disponivel else 'Indisponível'}"

    def save(self, *args, **kwargs):
        self.disponivel = self.quantidade > 0
        super().save(*args, **kwargs)

        
class NotaFiscal(models.Model):
    numero_de_nota = models.CharField(max_length=50,)

    class Meta:
        verbose_name = "Nota Fiscal"
        verbose_name_plural = "Notas Fiscais"
        
    def __str__(self):
         return f"{self.numero_de_nota}"