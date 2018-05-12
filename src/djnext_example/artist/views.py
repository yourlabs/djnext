import glom

from django import forms
from django.views import generic
from django.urls import reverse_lazy

from .models import Artist

FORM_SPEC = {
    'fields': [{
        'name': 'name',
        'label': 'label',
        'help_text': 'help_text',
    }],
}


class ArtistCreateView(generic.CreateView):
    model = Artist
    fields = ['name']
    template_name = 'create.js'

    def get_context_data(self):
        c = super().get_context_data()
        c['form'] = glom.glom(c['form'], FORM_SPEC)
        return c


class ArtistListView(generic.ListView):
    model = Artist
    template_name = 'list.js'

    def get_context_data(self):
        c = super().get_context_data()
        c['object_list'] = glom.glom(
            c['object_list'],
            dict(results=[dict(name='name')])
        )
        return c
