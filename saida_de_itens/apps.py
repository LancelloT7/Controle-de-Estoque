from django.apps import AppConfig


class SaidaDeItensConfig(AppConfig):
    name = 'saida_de_itens'
    def ready(self):
        import saida_de_itens.signals

