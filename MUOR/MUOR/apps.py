from django.apps import AppConfig


class MUORconfig(AppConfig):
    name = 'MUOR'

    def ready(self):
        import MUOR.signals
