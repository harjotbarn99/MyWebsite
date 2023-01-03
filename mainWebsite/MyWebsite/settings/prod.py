from .base import *

print("\n********************************************************************************\n starting app in Production\n********************************************************************************\n")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG_YAML["App"]["secret_key"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ["localhost"]


# required for staticlally collection file and only those files served by apache or nginx
STATIC_ROOT = Path.joinpath(SRC_PATH, "staticfiles")