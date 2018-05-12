from django.urls import include, path, re_path
from djnext.views import Proxy

urlpatterns = [
    path('', include('djnext_example.artist.urls')),
    re_path(r'^_next.*', Proxy.as_view()),
]
