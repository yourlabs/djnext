from django.views.generic import CreateView, ListView
from django.urls import path, reverse_lazy

from . import views


urlpatterns = [
    path(
        '',
        views.ArtistCreateView.as_view(),
        name='artist_create',
    ),
    path(
        'list',
        views.ArtistListView.as_view(),
        name='artist_list',
    ),
]
