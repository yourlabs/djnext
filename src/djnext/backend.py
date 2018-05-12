import os

from django.apps import apps
from django.conf import settings
from django.contrib.staticfiles import finders
from django.template import TemplateDoesNotExist
from django.template.backends.base import BaseEngine
from django.utils.module_loading import import_string

import requests


djnext = apps.get_app_config('djnext')
THREADLOCALS_MIDDLEWARE = 'threadlocals.middleware.ThreadLocalMiddleware'


class Backend(BaseEngine):
    def __init__(self, params):
        self.options = params.pop('OPTIONS')
        super().__init__(params)

    def from_string(self, template_code):
        raise NotImplemented()

    def get_template(self, template_name):
        target = 'pages/' + template_name
        result = finders.find(target, all=True)
        if not result:
            raise TemplateDoesNotExist(target, backend=self)
        return Template(path=result[0], backend=self)


class Template:
    def __init__(self, path, backend=None):
        self.path = path
        self.backend = backend

    def render(self, context=None, request=None):
        name = self.path.split('/')[-1][:-3]  # remove .js
        if not name.startswith('/'):
            name = '/' + name

        context = context or {}

        context_processors = djnext.options.get('context_processors', [])
        for cp_name in context_processors:
            cp = import_string(cp_name)
            if THREADLOCALS_MIDDLEWARE in settings.MIDDLEWARE:
                from threadlocals.threadlocals import get_current_request
                request = get_current_request()
            else:
                request = None

            context.update(cp(request))
        print(context)

        return requests.get(
            self.backend.options['NEXTJS_DSN'] + name
        ).content
