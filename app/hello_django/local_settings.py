import os

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": 'hello_django_prod',
        "USER": 'hello_django',
        "PASSWORD": 'hello_django',
        "HOST": '192.168.100.14',
        "PORT": 5432,
    }
}
