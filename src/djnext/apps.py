from django.apps import apps


class DefaultAppConfig(apps.AppConfig):
    def ready(self):
        pass
