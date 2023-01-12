from .base import *

print("\n********************************************************************************\n starting app in Production\n********************************************************************************\n")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG_YAML["App"]["secret_key"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


