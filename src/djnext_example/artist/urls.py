from django.views.generic import CreateView, ListView
from django.urls import path, reverse_lazy

from .models import Artist


urlpatterns = [
    path(
        '',
        CreateView.as_view(
            model=Artist,
            fields=['name'],
            success_url=reverse_lazy('artist_list'),
            template_name='create.js',
        ),
        name='artist_create',
    ),
    path(
        'list',
        ListView.as_view(model=Artist, template_name='list.js'),
        name='artist_list',
    ),
]
