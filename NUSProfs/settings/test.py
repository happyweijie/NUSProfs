from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Use a separate test database URL or config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('TEST_DB_NAME', 'testdb'),
        'USER': os.getenv('TEST_DB_USER', 'testuser'),
        'PASSWORD': os.getenv('TEST_DB_PASSWORD', 'testpassword'),
        'HOST': os.getenv('TEST_DB_HOST', 'localhost'),
        'PORT': os.getenv('TEST_DB_PORT', '5432'),
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}