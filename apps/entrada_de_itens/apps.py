# entrada_de_itens/apps.py
from django.apps import AppConfig

class EntradaDeItensConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entrada_de_itens'

    def ready(self):
        # aqui você importa seu módulo de signals
        import entrada_de_itens.signals
    