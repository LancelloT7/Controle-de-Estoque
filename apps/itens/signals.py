from django.db.models.signals import post_save
from django.dispatch import receiver
from saida_de_itens.models import Saida


@receiver(post_save, sender=Saida)
def atualizar_ultima_saida(sender, instance, created, **kwargs):
    if created:
        item = instance.item
       
        item.ultima_saida = instance.data.date()  
        item.save(update_fields=['ultima_saida'])