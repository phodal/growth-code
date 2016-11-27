import os
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'growth_studio',
        'USER': 'root',
        'PASSWORD': 'phodal',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}