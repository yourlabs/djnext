import os

import django12factor
globals().update(django12factor.factorise())

SECRET_KEY = os.environ.get('SECRET_KEY', 'notsecret')

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
WSGI_APPLICATION = 'djnext_example.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'djnext.backend.Backend',
        'OPTIONS': {
            'context_processors': [
                'djnext_example.artist.context_processors.menu',
            ]
        },
    }
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'
