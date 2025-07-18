from .base import *

DEBUG = False

ALLOWED_HOSTS = ['nusprofs-api.onrender.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Allow only your Vercel frontend to access API views
CORS_ALLOW_ALL_ORIGINS = True
