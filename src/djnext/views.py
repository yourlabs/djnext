from django import http
from django.apps import apps
from django.conf import settings
from django.views.generic import View

import requests

from .utils import context_process


djnext = apps.get_app_config('djnext')


class State(View):
    def get(self, request, *args, **kwargs):
        return http.JsonResponse(context_process())


class Proxy(View):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        for name, value in self.get_extra_headers().items():
            response[name] = value
        return response

    def get_extra_headers(self):
        dsn = None

        parts = self.request.get_raw_uri().split('/')
        new = '/'.join(parts[:3])
        for host in settings.ALLOWED_HOSTS:
            if host == '*' or host == parts[3]:
                dsn = new

        if dsn is None:
            raise Exception('ALLOWED_HOSTS does not allow ' + parts[3])

        return {
            'Access-Control-Allow-Headers': dsn,
            'Access-Control-Allow-Methods': 'OPTIONS, GET',
            'Access-Control-Allow-Origin': dsn,
            'Access-Control-Allow-Method': dsn,
        }


    def get(self, request, *args, **kwargs):
        url = djnext.options['NEXTJS_DSN'] + request.path + '?' + request.GET.urlencode()

        if request.META.get('HTTP_ACCEPT', None) == 'text/event-stream':
            response = requests.get(url, stream=True)
            ret = http.StreamingHttpResponse(response.iter_content())
        else:
            response = requests.get(url)
            ret = http.HttpResponse(
                content=bytes(response.content),
            )

        ret['Content-Type'] = response.headers['Content-Type']
        return ret
