# My website

# Deployed info
the website is deployed at http://172.104.12.50/ .
to see how the website is dynamic 
- go to http://172.104.12.50/admin 
- use `viewer` and `password1@` to access to admin panel
you will only have read access while I can modify the fields in admin panel to change the website and it requires no coding skills

# Note
If anyone would like to work on the frontend of this website, please contact me at harjotbarn99@gmail.com
The app has been tested to work with 
- python 
  - 3.10.8
  - 3.8
- node 
  - 16.17.1 
  - 19.4.0
if you face any isses with dependencies try updating python and node or using the specified versions

## Before use
- create the config.yaml file
config vars  in `config.yaml` file. you can copt the below code paste it in your file and change the variables

```
App:
  prod : false        # determins if the app should startup in production or development
  secret_key : 'django-insecure-fhjg$b5@3%$_6viw@x^fca4=s!4xm+z5(#nh=*(8h^l*44t)un-modified for prod' # secret key used for production
  superuser_username : "admin"      # the superuser username used by makesuper command
  superuser_password : "admin1233"       # the superuser password used by makesuper command
  superuser_email : "admin@xyzdomain.com"       # the superuser email used by makesuper command
  debug : false        # if run in debug mode or not
  allowed_hosts_dev : ["127.0.0.1"]         # hosts allowed for development by django
  allowed_hosts_prod : ["127.0.0.1"]          # hosts allowed for production by django
```

- if you have a db backup put it in `/mainWebsite` as `backup_db.json`
the `setup.sh` will ask you if it should load the back up or not but you can do it manually too using `python manage.py loaddata backup_db.json`


## For Using
- run the `setup.sh` file 

### To remember 
always make sure you are using the python virtual env ot this app otherwise the app might not work.

## For deployment
go to https://techtutorguro.com/how-to-install-django-3-2-lts-on-ubuntu-20-04/
if you face any issues while visiting the deployed app (you get error 500) then turn debug on and try again to see more info which  an help you figure out the issues

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
+ to hide debug toolbar go to `<projectName>/settings/__init__.py` and find the function `show_toolbar` and make it `return False`


# Useful info
- remove the `statc/dist` folder and uncomment it in `.gitignore` . this will not push the built files and saves space
- add apps to `<projectName>/settings/__init__.py` after creating them
- be careful while naming css and scss files `app.scss` compiles to `app.css` so be careful not to name a css file same as scss



