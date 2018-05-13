import json
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
    'errors': []
}


class ArtistCreateView(generic.CreateView):
    model = Artist
    fields = ['name']
    template_name = 'create.js'

    def get_context_data(self, *a, **k):
        c = super().get_context_data(*a, **k)
        form = c['form']
        c['form'] = glom.glom(c['form'], FORM_SPEC)
        print('FORM VALID ===', form.is_valid())
        return c

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == 'POST' and self.request.META.get('HTTP_ACCEPT') == 'application/json':
            kwargs['data'] = json.loads(self.request.body)
        print('DATA', kwargs.get('data', None))
        # kwargs['data'] = json.loads(self.request.body)
        return kwargs

    def form_valid(self, form):
        return http.JsonResponse(dict(
            redirect=reverse_lazy('artist_list'),
        ))

    def form_invalid(self, form):
        return http.JsonResponse(glom.glom(c['form'], FORM_SPEC))


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
