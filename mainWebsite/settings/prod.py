from .base import *
import os
import django_heroku

ALLOWED_HOSTS = ["harjot-barn.herokuapp.com"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = os.environ.get("SECRET_KEY")

STATIC_ROOT = os.path.join(BASE_DIR, "static")

# database
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": os.environ("PDB_NAME"),
#         "USER": os.environ("PDB_USER"),
#         "PASSWORD": os.environ("PDB_PASS"),
#         "HOST": "localhost",
#         "PORT": "",
#     }
# }

django_heroku.settings(locals())