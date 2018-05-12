import imp
import os

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils import autoreload


def gen_filenames(only_new=False):
    paths = []
    for app_name in settings.INSTALLED_APPS:
        parts = app_name.split('.')
        mod = parts.pop(0)
        mod_path = imp.find_module(mod)[1]
        path = mod_path
        if parts:
            path += '/' + os.path.join(*parts)
        path += '/static'
        if os.path.isdir(path):
            for root, directories, filenames in os.walk(path):
                for filename in filenames:
                    if filename.startswith('.'):
                        continue
                    paths.append(os.path.join(root, filename))
    return paths


old_gen_filename = autoreload.gen_filenames
autoreload.gen_filenames = gen_filenames


class Command(BaseCommand):
    def handle(self, *args, **options):
        autoreload.main(self.inner_run, None, options)

    def inner_run(self, *args, **options):
        # If an exception was silenced in ManagementUtility.execute in order
        # to be raised in the child process, raise it now.
        autoreload.raise_last_exception()
        settings.STATIC_ROOT = 'static_root'
        source = os.path.join(os.getcwd(), 'static_root/pages')
        target = os.path.join(os.getcwd(), 'pages')

        if not os.path.islink(target):
            os.symlink(source, target)

        try:
            call_command('collectstatic', link=True, interactive=False)
        except FileNotFoundError as e:
            print(e)
