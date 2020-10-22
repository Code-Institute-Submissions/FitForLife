#!/bin/bash
export DEVELOPMENT="True"
export HEROKU="False"
export SECRET_KEY="MySecretKey"
export HEROKU_POSTGRES="False"
#export DATABASE_URL="postgres://bmhukkzcvbrudo:f0efd09b91a12d869dad3cd600e90906bf522e82621b6a4b7a3712c992d8a209@ec2-54-246-115-40.eu-west-1.compute.amazonaws.com:5432/dcr08rj67p5k70"
# passing -k suppresses database
python3 manage.py test product.test_models

 
