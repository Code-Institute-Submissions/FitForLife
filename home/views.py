  
from django.shortcuts import render
from django.conf import settings
import logging

# Create your views here.


def index(request):
    """ A view to return the index page """
    if settings.DEBUG:
        logger = logging.getLogger('django') #name specifies the module name
        logger.warn('Main Page:' )
    return render(request, 'home/index.html')