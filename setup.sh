#! /bin/bash

source ./setupHelp/functions.sh 

printProper "installing node packages"
# this installs all the node packages required to run the app
npm install
printProper "building static packages"
# this builds the static files like css js and images to server for the app
gulp build

printProper "setting up python virtual environment"
FILE=./websiteVenv/bin/activate
if ! test -f "$FILE"; then
    python3 -m venv websiteVenv
    source websiteVenv/bin/activate
    pip install -r requirements.txt
else 
    echo "already setup"
    source websiteVenv/bin/activate
fi


printProper "checking for `config.yaml` file"
FILE=./config.yaml
if ! test -f "$FILE"; then
    echo
    echo "$FILE does not exist"
    echo "please create one with all required variables. Program is exiting !"
    exit
fi

printProper "setting up django website " 
cd mainWebsite
python manage.py migrate
echo "creating super user"
python manage.py makesuper

FILE=./backup_db.json
if test -f "$FILE"; then
    read -n1 -p "press y to populate data from backup_db.json : " key_input
    if [ "$key_input" == "y" ] ; then
        python manage.py loaddata backup_db.json
    fi
fi

echo 
echo
read -n1 -p "press y to setup production : " key_input
if [ "$key_input" == "y" ] ; then
    python manage.py collectstatic
fi

echo 
echo
echo "done ..... !!!"
