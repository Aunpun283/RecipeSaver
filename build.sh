#!/usr/bin/env bash
# exit on error

pip install -r reqs.txt
pip install --upgrade pymongo bson
python manage.py collectstatic --no-input
python manage.py migrate
 
