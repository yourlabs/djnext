import hashlib
import json
import os

from django.apps import apps
from django.conf import settings
from django.contrib.staticfiles import finders
from django.template import TemplateDoesNotExist
from django.template.backends.base import BaseEngine

import requests

from .utils import context_process, state_process


djnext = apps.get_app_config('djnext')


class Backend(BaseEngine):
    def __init__(self, params):
        self.options = params.pop('OPTIONS')
        super().__init__(params)

    def from_string(self, template_code):
        return Template(code=template_code, backend=self)

    def get_template(self, template_name):
        target = 'pages/' + template_name
        result = finders.find(target, all=True)
        if not result:
            raise TemplateDoesNotExist(target, backend=self)
        return Template(path=result[0], backend=self)


class Template:
    def __init__(self, path=None, code=None, backend=None):
        self.path = path
        self.code = code
        self.backend = backend

        if self.code and not self.path:
            name = hashlib.md5(self.code).encode('utf-8').hexdigest()
            print('Rendering', name, 'for', self.code)
            self.path = os.path.join('pages', name)

        if self.code and not os.path.exists(self.path):
            with open(self.path, 'w+') as f:
                print('WRITING', self.path)
                f.write(self.code)

    def render(self, context=None, request=None):
        name = self.path.split('/')[-1][:-3]  # remove .js
        if not name.startswith('/'):
            name = '/' + name

        state = context_process(context)

        response = requests.get(
            self.backend.options['NEXTJS_DSN'] + name,
            dict(state=json.dumps(state))
        )

        print('REQUEST', self.backend.options['NEXTJS_DSN'] + name)
        print('state=', state)
        print('RESPONSE headers', response.headers)
        print('RESPONSE content', response.content)

        return response.content
