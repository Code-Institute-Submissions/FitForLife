  
from django.shortcuts import render
from django.conf import settings
import logging
from django.conf.urls.static import static

# A default Handler for pages not found
# this uses the templates in templates/404.html
def handler404(request, exception):
    """ returns a custom 404 template for pages not found """
    return render(request, "404.html", status=404)


# A default Handler for 500 errors
# The 500 Internal Server Error is a very general HTTP status code
# that means something has gone wrong on the web site's server but 
# the server could not be more specific on what the exact problem was.
# this uses the templates in templates/500.html
def handler500(request):
    """ return a custom 500 template  for internal server errors"""
    return render(request, "500.html", status=500)



def index(request):
    """ A view to return the index page """
    if settings.DEBUG:
        logger = logging.getLogger('django') #name specifies the module name
        logger.warn('Main Page:' )
    return render(request, 'home/index.html')