import os

from .base import *   # производственная среда

DEBUG = False       # Закрывает информацию о проекте от злоумышленников

ADMINS = [
    ('admin', 'dr.ararturovich@gmail.com'), # будут отправлены исключения людям в данном списке
]

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com'] # указываются хосты которым будет разрешена раздача приложения

DATABASES = {         # Указываем базу данных для производственной среды
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,

    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]


# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True