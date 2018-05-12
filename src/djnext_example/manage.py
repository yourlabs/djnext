import os
import sys
import warnings


def main(settings_module=None):
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        settings_module or 'djnext_example.settings'
    )

    if 'DEBUG' not in os.environ:
        warnings.warn('DEFAULTING DEBUG=1')
        os.environ.setdefault('DEBUG', '1')

    if 'ALLOWED_HOSTS' not in os.environ:
        warnings.warn('DEFAULTING ALLOWED_HOSTS=*')
        os.environ.setdefault('ALLOWED_HOSTS', '*')

    if 'DATABASE_URL' not in os.environ:
        os.environ.setdefault(
            'DATABASE_URL',
            'sqlite:///{}/.djnext_example.sqlite'.format(os.getenv('HOME'))
        )
        warnings.warn('DEFAULTING DATABASE_URL=' + os.getenv('DATABASE_URL'))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Couldn\'t import Django. Are you sure it\'s installed and '
            'available on your PYTHONPATH environment variable? Did you '
            'forget to activate a virtual environment?'
        ) from exc
    execute_from_command_line(sys.argv)
