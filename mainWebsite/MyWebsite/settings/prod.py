from .base import *

print("\n********************************************************************************\n starting app in Production\n********************************************************************************\n")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG_YAML["App"]["secret_key"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = CONFIG_YAML["App"]["debug"]


ALLOWED_HOSTS = CONFIG_YAML["App"]["allowed_hosts_prod"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


