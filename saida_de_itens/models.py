from django.db import models
from itens.models import Item, Fabricante
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

class Saida(models.Model):

    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
         return f"{self.data:%Y-%m-%d %H:%M} — {self.item.nome} (-{self.quantidade})"
    
    def clean(self):
        if self.item.quantidade < self.quantidade:
            raise ValidationError(f"Estoque insuficiente para o item '{self.item.nome}'.")

    def save(self, *args, **kwargs):
        self.full_clean()  # chama clean() para validar antes de salvar
        super().save(*args, **kwargs)        