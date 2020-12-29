release: yarn install && yarn run build && python manage.py migrate 

web: gunicorn mainWebsite.wsgi 
