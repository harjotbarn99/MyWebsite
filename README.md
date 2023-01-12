# My website

## Before use
- create the config.yaml file
config vars  in `config.yaml` file. you can copt the below code paste it in your file and change the variables

```
App:
  prod : false  # determins if the app should startup in production or development
  secret_key : 'django-insecure-fhjg$b5@3%$_6viw@x^fca4=s!4xm+z5(#nh=*(8h^l*44t)un-modified for prod' # secret key used for production
  superuser_username : "admin" # the superuser username used by makesuper command
  superuser_password : "admin1233"  # the superuser password used by makesuper command
  superuser_email : "admin@xyzdomain.com" # the superuser email used by makesuper command
  debug : false  # if run in debug mode or not
```

## Fo Using
run the `setup.sh` file 

## for deployment
```
python manage.py migrate
python manage.py collectstatic
gunicorn MyWebsite.wsgi 
```
you can add `--log-level=debug` flag to gunicorn to enable more info

## while development
- debug toolbar is very helpful 
- `gulp watch` to open up a session where if you make a change in static files the files will be built again and browser will be refersed (only on the url provided when you run `gulp watch`)


## config file
These are changed for the deployed server
access variables by 
```
from django.conf import settings

username_ = settings.CONFIG_YAML["App"]["var_name"]
```


# Custom commands
These commands are used like normal django commands like `python manage.py <command>  <args>`

### rename 
+ use this command to rename your project 
+ eg -> `python manage.py rename djBoilerplate newname`
+ eg -> `python manage.py rename oldname newname`

###  makesuper
+ this command make a super user useful when 
  + you clone a repository and start new
  + when you delete database and run make migrations
+ command -> `python manage.py makesuper`
+ before use it is recomended to change `superuser_username`, `superuser_password` and `superuser_email` in `config.yaml`
  
  

# Handling static files
Put all static files in folder static/src/<folder>
then use `gulp build` and all you files will be avalible 

To get a static file use `{% static '<folder>/<file>' %}` as url also remember to use the `{% load static %}`

eg 
```
{% load static %}
{% static 'js/index.js' %}
{% static 'other/my.pdf' %}
{% static 'img/index.js' %}
```


# Debug toolbar
+ to hide debug toolbar go to `<projectName>/settings/dev.py` and find the function `show_toolbar` and make it `return False`


# Useful info
- remove the `statc/dist` folder and uncomment it in `.gitignore` . this will not push the built files and saves space
- add apps to `<projectName>/settings/base.py` after creating them
- be careful while naming css and scss files `app.scss` compiles to `app.css` so be careful not to name a css file same as scss



