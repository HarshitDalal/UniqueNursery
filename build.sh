#!/bin/bash

# Buliding the project
eche "Buliding the project"
python3.10 -m pip install -r requirements.txt

# make migrations 
echo "Make migrations"
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput

echo "Collect Static files"
python3.10 manage.py collectstatic --noinput --clear
