from django.db import models
from itens.models import Item, Fabricante, NotaFiscal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.

class Entrada(models.Model):

    nota_fiscal = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE, verbose_name="Origem")
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return f"{self.nota_fiscal.numero_de_nota}-{self.data:%Y-%m-%d %H:%M} — {self.item.nome} (+{self.quantidade})"
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.responsavel = request.user
        super().save_model(request, obj, form, change)