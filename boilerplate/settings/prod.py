from .base import *
import os

ALLOWED_HOSTS = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ("SECRET_KEY")


# database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ("PDB_NAME"),
        "USER": os.environ("PDB_USER"),
        "PASSWORD": os.environ("PDB_PASS"),
        "HOST": "localhost",
        "PORT": "",
    }
}
