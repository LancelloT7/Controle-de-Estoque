from django.apps import AppConfig

class SeuAppConfig(AppConfig):
    name = 'itens'

    def ready(self):
        import itens.signals  # importa e conecta os signals
