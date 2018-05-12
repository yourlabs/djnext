import copy

from django.apps import apps
from django.conf import settings
from django.utils.module_loading import import_string

djnext = apps.get_app_config('djnext')
THREADLOCALS_MIDDLEWARE = 'threadlocals.middleware.ThreadLocalMiddleware'


def context_process(context=None):
    context = copy.copy(context) or {}
    context_processors = djnext.options.get('context_processors', [])
    for cp_name in context_processors:
        cp = import_string(cp_name)
        if THREADLOCALS_MIDDLEWARE in settings.MIDDLEWARE:
            from threadlocals.threadlocals import get_current_request
            request = get_current_request()
        else:
            request = None

        context.update(cp(request))

    for key, value in context.items():
        try:
            json.dumps(value)
        except:
            print('Cannot JSON parse key', key, 'with value', value)
        else:
            context.pop(key)
    return context
