from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Saida

@receiver(post_save, sender=Saida)
def remover_item(sender, instance, created, **kwargs):
    if created:
        item = instance.item
        # subtrai sem deixar negativo
        item.quantidade = max(item.quantidade - instance.quantidade, 0)
        item.save()  # vai recalcular `disponivel` no save de Item
