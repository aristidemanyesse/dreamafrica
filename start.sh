#!/bin/bash

service cron start
yes | venv/bin/python manage.py makemigrations
yes | venv/bin/python manage.py migrate
venv/bin/python manage.py crontab add
venv/bin/python manage.py runserver 0.0.0.0:8000
