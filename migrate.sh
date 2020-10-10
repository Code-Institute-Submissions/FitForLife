#!/bin/bash
export DEVELOPMENT="True"
export HEROKU="False"
export HEROKU_POSTGRES="True"
python3 manage.py makemigrations
python3 manage.py migrate