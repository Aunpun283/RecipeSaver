#!/usr/bin/env bash
# exit on error

 
pip install -r reqs.txt
python manage.py collectstatic --no-input
python manage.py migrate
 
