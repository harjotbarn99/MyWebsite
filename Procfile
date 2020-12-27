release: node install && node run build && python manage.py migrate 
web: gunicorn mainWebsite.wsgi 