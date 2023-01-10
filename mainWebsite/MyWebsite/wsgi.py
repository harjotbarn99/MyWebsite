"""
WSGI config for MyWebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyWebsite.settings')

application = get_wsgi_application()

from django.conf import settings

if settings.DEBUG == False :
        
    from whitenoise import WhiteNoise
    print("\n src path  -> ", settings.STATIC_ROOT, " and debug = ", settings.DEBUG)
    application = WhiteNoise(application, root=settings.STATIC_ROOT)
    application.add_files(settings.STATIC_ROOT, prefix="/static/")
    application.add_files(settings.MEDIA_ROOT, prefix="/media/")