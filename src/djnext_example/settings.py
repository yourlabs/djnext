import os

import django12factor
globals().update(django12factor.factorise())

STATIC_ROOT="static_root"
'''

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djnext_example',  # load layout template
    'djnext_example.artist',  # example app in this directory

    'djnext',  # for isomorphic code love

    'crudlfap',  # for dev command
]

ROOT_URLCONF = 'djnext_example.urls'

TEMPLATES = [
    {
        'BACKEND': 'djnext.Backend',
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djnext_example.wsgi.application'

SECRET_KEY = os.environ.get('SECRET_KEY', 'notsecret')

STATIC_URL = '/static/'
