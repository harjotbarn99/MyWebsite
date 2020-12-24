from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# secret key
SECRET_KEY = "dev*)!1_ze_+9vvcc45c8u9l)b!hjcw7zajel!g@_6%ml#jb5peb"


# database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# debug toolbar
INSTALLED_APPS += [
    "debug_toolbar",
    "mail_panel",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.timer.TimerPanel",
    "mail_panel.panels.MailToolbarPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    # "djdt_flamegraph.FlamegraphPanel",
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

# EMAIL_BACKEND = "mail_panel.backend.MailToolbarBackend"
# MAIL_TOOLBAR_TTL = 86400  # 1 Day


# email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
