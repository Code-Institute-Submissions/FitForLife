#!/bin/sh
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 app name" >&2
  exit 1
fi
APP_NAME=$1
APP_DIRECTORY=${APP_NAME}
python manage.py startapp $APP_NAME
echo "Create a tests directory: $APP_DIRECTORY/tests"
mkdir $APP_DIRECTORY/tests
echo "Create a templates directory $APP_DIRECTORY/templates/$APP_NAME"
mkdir -p $APP_DIRECTORY/templates/$APP_NAME
echo "Create a templates include directory $APP_NAME/templates/$APP_NAME"
mkdir -p $APP_DIRECTORY/templates/$APP_DIRECTORY/includes
echo "Create a custom widgets directory $APP_DIRECTORY/templates/$APP_NAME"
mkdir -p $APP_DIRECTORY/templates/$APP_DIRECTORY/custom_widegt_templates
#copy in some sample code from products
cp products/templates/products/products.html  $APP_DIRECTORY/templates/$APP_DIRECTORY/$APP_DIRECTORY.html
echo "add an entry to settings.py: INSTALLED_APPS = [     'products.${APP_NAME}.${APP_NAME}Config',"
echo "Add an entry to urls.py: path('$APP_DIRECTORY/', include('$APP_DIRECTORY.urls')),"mkdir 
rm $APP_DIRECTORY/tests.py
printf "from django.contrib import admin\nfrom .models import $APP_DIRECTORY\n# Register your models here.\nclass ${APP_NAME}Admin(admin.ModelAdmin):\nlist_display = ()\nadmin.site.register($APP_NAME, ${APP_NAME}Admin)" > ${APP_NAME}/admin.py 


