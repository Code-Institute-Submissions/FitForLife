#!/bin/bash
export DEVELOPMENT="True"
export HEROKU="False"
export SECRET_KEY="secretkeyfordjango"
export HEROKU_POSTGRES="True"
export DATABASE_URL="postgres://mtajlhnjsvfhxr:56013e42e5b515c8c488fd890f4aa2351f4f47e6b39ed926703339ead2d6fd64@ec2-54-170-123-247.eu-west-1.compute.amazonaws.com:5432/db6esjaiarmhtb"
python3 manage.py runserver
 
