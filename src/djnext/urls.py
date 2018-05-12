from django.urls import path, re_path

from .views import Proxy, State


urlpatterns = [
    path('state', State.as_view(), name='djnext_state'),
    re_path(r'.*', Proxy.as_view(), name='djnext_proxy'),
]
