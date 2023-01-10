# Django boiler plate

This repo is upto date with Django 4.1.5

for any bugs, issues or suggsetions contact me at harjotbarn99@gmail.com


## Why use this ?
- can serve static files 
- can build scss 
- can run in dev and production setting setup
- has custom commad examples and
  - make super user with the custom command provided (no need to fill in username password and email)
- has setup configuration variable
- has debug toobar 

all of this with just a few commands



## To Use
- clone or download this project as zip(recommended)
- run virtual environment (First) `pipenv install --dev`
- rename the project `python manage.py rename djBoilerplate theBestApp`  =>  `python manage.py rename <current name> <new name>`. 
- `npm install` to install npm packages
- `gulp build` to build static files
- `python manage.py make migrations`
- `python manage.py makesuper` creates the superuser
- `python manage.py runserver`

### Before deploying
- change details in package.json 
- change all config variables in `config.yaml`

### security 
if you are going to push you code to github it is recommended to 
- remove the `config.yaml` file and uncomment it in `.gitignore` . this will prevent putting sensitive info onto github 


## while development
- debug toolbar is very helpful 
- `gulp watch` to open up a session where if you make a change in static files the files will be built again and browser will be refersed (only on the url provided when you run `gulp watch`)


## config
access variables by 
```
from django.conf import settings

username_ = settings.CONFIG_YAML["App"]["var_name"]
```
current config vars 
App:
  prod : false  -> determins if the app should startup in production or development
  secret_key : 'django-insecure-fhjg$b5@3%$_6viw@x^fca4=s!4xm+z5(#nh=*(8h^l*44t)un-modified for prod' -> secret key used for production
  superuser_username : "admin" -> the superuser username used by makesuper command
  superuser_password : "admin1233" -> the superuser password used by makesuper command
  superuser_email : "admin@xyzdomain.com" -> the superuser email used by makesuper command


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
- remove the `media` folder and uncomment it in `.gitignore`. this folder stores files uploaded by users so no need to push it to git
- add apps to `<projectName>/settings/base.py` after creating them
- be careful while naming css and scss files `app.scss` compiles to `app.css` so be careful not to name a css file same as scss



