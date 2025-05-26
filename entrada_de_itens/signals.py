# itens/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Entrada, Item

@receiver(post_save, sender=Entrada)
def adicionar_item(sender, instance, created, **kwargs):
    if created:
        item = instance.item
        item.quantidade += instance.quantidade
        item.save()
    