from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from .validators import validar_tamanho_imagem

# Create your models here.
class Fabricante(models.Model):
    nome_do_fabricante = models.CharField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome_do_fabricante

class Item(models.Model):

    sku = models.CharField(max_length=50, unique=False, null=False, blank=False)
    fabricante = models.ForeignKey('Fabricante', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    modelo = models.CharField(max_length=50, unique=False, null=False, blank=False)
    partnumber = models.CharField(max_length=50, unique=True, null=True, blank=True)
    img = models.ImageField(upload_to='itens/', blank=True, validators=[validar_tamanho_imagem])
    quantidade = models.PositiveIntegerField(default=0)
    endereco = models.CharField(max_length=50, unique=True, null=False, blank=False)
    disponivel = models.BooleanField(default=False)
    valor_atual = models.DecimalField(decimal_places=2, max_digits=15, verbose_name="Valor Hoje")

    def total_estoque(self):
        return self.quantidade*self.valor_atual

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    def __str__(self):
        return f"{self.sku}-{self.nome}-{self.modelo} ({self.fabricante}) - {self.quantidade} unidades - {'Disponível' if self.disponivel else 'Indisponível'}"

    def save(self, *args, **kwargs):
        self.disponivel = self.quantidade > 0
        super().save(*args, **kwargs)

        
class NotaFiscal(models.Model):
    numero_de_nota = models.CharField(max_length=50, verbose_name="Tipo de Origem")

    class Meta:
        verbose_name = "Origem"
        verbose_name_plural = "Origem"

    def __str__(self):
         return f"{self.numero_de_nota}"
    

class HistoricoValorItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="historico_valores")
    valor_anterior = models.DecimalField(decimal_places=2, max_digits=15)
    valor_novo = models.DecimalField(decimal_places=2, max_digits=15)
    data_alteracao = models.DateTimeField(auto_now_add=True)
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.item.nome} - {self.valor_anterior} → {self.valor_novo} ({self.data_alteracao.date()})"   

  