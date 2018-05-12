from django import http
from django.views.generic import View

import requests


class Proxy(View):
    def get(self, request, *args, **kwargs):
        from pprint import pprint
        response = requests.get('http://localhost:3000' + request.path + '?' + request.GET.urlencode())
        ret = http.HttpResponse(
            content=bytes(response.content),
        )
        ret['Access-Control-Allow-Headers'] = 'http://localhost:8000'
        ret['Access-Control-Allow-Methods'] = 'OPTIONS, GET'
        ret['Access-Control-Allow-Origin'] = 'http://localhost:8000'
        ret['Access-Control-Allow-Method'] = 'http://localhost:8000'
        ret['Content-Type'] = response.headers['Content-Type']
        return ret
