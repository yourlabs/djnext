import os

from django import apps
from django.conf import settings


class DefaultAppConfig(apps.AppConfig):
    name = 'djnext'
    module_name = 'djnext.backend.Backend'

    def set_settings(self):
        self.settings = None
        for b in settings.TEMPLATES:
            if b.get('BACKEND', None) == self.module_name:
                self.settings = b

    def set_options(self):
        self.set_settings()
        if not self.settings:
            settings.TEMPLATES.insert(0, dict(
                BACKEND=self.module_name,
                NAME='djnext',
            ))
            self.set_settings()

        self.settings.setdefault('OPTIONS', {})
        self.options = self.settings['OPTIONS']
        self.options.setdefault(
            'NEXTJS_DSN',
            os.getenv('NEXTJS_DSN', 'http://localhost:3000')
        )

    def ready(self):
        self.set_options()
