from .settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kazalive',
        'USER': 'root',
        'PASSWORD': 'Ruby2013'
    }
}

ALLOWED_HOSTS = ['admin.kaza.live']