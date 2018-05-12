from django.urls import include, path

urlpatterns = [
    path('', include('djnext_example.artist.urls')),
    path('_next/', include('djnext.urls')),
]
