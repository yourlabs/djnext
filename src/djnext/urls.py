from django.urls import re_path

from .views import Proxy


urlpatterns = [re_path(r'.*', Proxy.as_view())]
