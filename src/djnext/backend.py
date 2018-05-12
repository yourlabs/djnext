from django.contrib.staticfiles import finders
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy

import requests


class Backend(BaseEngine):
    # Name of the subdirectory containing the templates for this engine
    # inside an installed application.
    app_dirname = 'pages'

    def __init__(self, params):
        params = params.copy()
        options = params.pop('OPTIONS').copy()
        super().__init__(params)

    def from_string(self, template_code):
        try:
            return Template(code=template_code)
        except exc:
            raise TemplateSyntaxError(exc.args)

    def get_template(self, template_name):
        target = 'pages/' + template_name
        result = finders.find(target, all=True)
        if not result:
            raise TemplateDoesNotExist(target, backend=self)
        return Template(path=result[0])
        '''
        except foobar.TemplateCompilationFailed as exc:
            raise TemplateSyntaxError(exc.args)
            '''


class Template:

    def __init__(self, path, code=None):
        print(path, code)
        self.path = path
        self.code = code

    def render(self, context=None, request=None):
        name = self.path.split('/')[-1][:-3]  # remove .js
        return requests.get('http://localhost:3000/' + name).content
